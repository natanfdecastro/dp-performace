from sys import path
import parser_txt_knapsack

path.append('src.main.python.edu.tec.ic6400')


def knapsack_bottom_up(total_weight, items_weights, benefits, len, iterations):
    for _ in range(0, int(iterations)):
        knapsack_solutions = [[0 for x in range(total_weight + 1)] for _ in range(len + 1)]

        for i in range(len + 1):
            for w in range(total_weight + 1):
                if i == 0 or w == 0:
                    knapsack_solutions[i][w] = 0
                elif items_weights[i - 1] <= w:
                    knapsack_solutions[i][w] = max(benefits[i - 1]
                                                   + knapsack_solutions[i - 1][w - items_weights[i - 1]],
                                                   knapsack_solutions[i - 1][w])
                else:
                    knapsack_solutions[i][w] = knapsack_solutions[i - 1][w]

        answer = knapsack_solutions[len][total_weight]
        print("Beneficio máximo: ", answer)
        included = []
        total_weight_temp = total_weight
        for i in range(len, 0, -1):
            if answer <= 0:
                break

            if answer == knapsack_solutions[i - 1][total_weight_temp]:
                continue
            else:

                included.append(i)

                answer = answer - benefits[i - 1]
                total_weight_temp = total_weight_temp - items_weights[i - 1]

        included.sort()
        print("Incluidos: ", str(included)[1:-1])


def knapsack_top_down():
    print("top down")


def routines_brute_force(total_weight, items_weights, benefits, capacity, iterations):

    for _ in range(int(iterations)):
        included = []

        answer, included = knapsack_brute_force(total_weight, items_weights, benefits, capacity, included)
        print("Beneficio máximo: ", answer)
        print("Incluidos: ", str(included)[1:-1])


def knapsack_brute_force(total_weight, items_weights, benefits, len, included):

    if len == 0 or total_weight == 0:
        return 0, included

    if items_weights[len - 1] > total_weight:
        return knapsack_brute_force(total_weight, items_weights, benefits, len - 1, included)

    else:
        sum_1, included_temp1 = knapsack_brute_force(total_weight - items_weights[len - 1], items_weights, benefits,
                                                     len - 1, [len] + included)
        sum_1 += benefits[len - 1]
        sum_2, included_temp2 = knapsack_brute_force(total_weight, items_weights, benefits, len - 1, included)

        if sum_1 > sum_2:
            return sum_1, included_temp1
        else:
            return sum_2, included_temp2
