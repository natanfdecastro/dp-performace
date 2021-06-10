from sys import path
import parser_txt_knapsack

path.append('src.main.python.edu.tec.ic6400')


def knapsack_bottom_up(total_weight, items_weights, benefits, capacity, iterations):
    for _ in range(0, int(iterations)):
        knapsack_solutions = [[0 for x in range(total_weight + 1)] for _ in range(capacity + 1)]

        for i in range(capacity + 1):
            for w in range(total_weight + 1):
                if i == 0 or w == 0:
                    knapsack_solutions[i][w] = 0
                elif items_weights[i - 1] <= w:
                    knapsack_solutions[i][w] = max(benefits[i - 1]
                                                   + knapsack_solutions[i - 1][w - items_weights[i - 1]],
                                                   knapsack_solutions[i - 1][w])
                else:
                    knapsack_solutions[i][w] = knapsack_solutions[i - 1][w]

        answer = knapsack_solutions[capacity][total_weight]
        print("Beneficio máximo: ", answer)
        included = []
        total_weight_temp = total_weight
        for i in range(capacity, 0, -1):
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


# Matrix use to memoization of top down approach
memoize_top_down = []


# values setter for knapsack with top down approach
def knapsack_top_down(max_weigth, weigths, benefits, capacity, iterations):
    memo = [[0 for i in range(max_weigth + 1)] for j in range(capacity + 1)]

    for i in memo:
        memoize_top_down.append(i)

    for i in range(int(iterations)):
        print("Beneficio Maximo: ", __knapsack(weigths, benefits, max_weigth, capacity))
        print("Incluidos: ", str(__get_list_benefits(benefits, weigths, capacity, max_weigth))[1:-1])


# knapsack with top down approach
def __knapsack(weigths, benefits, max_weigth, capacity):
    # base conditions
    if capacity == 0 or max_weigth == 0:
        return 0
    if memoize_top_down[capacity][max_weigth] != 0:
        return memoize_top_down[capacity][max_weigth]

    # choice diagram code
    if weigths[capacity - 1] <= max_weigth:
        memoize_top_down[capacity][max_weigth] = max(
            benefits[capacity - 1] + __knapsack(weigths, benefits, max_weigth - weigths[capacity - 1], capacity - 1),
            __knapsack(weigths, benefits, max_weigth, capacity - 1))
        return memoize_top_down[capacity][max_weigth]

    elif weigths[capacity - 1] > max_weigth:
        memoize_top_down[capacity][max_weigth] = __knapsack(weigths, benefits, max_weigth, capacity - 1)
        return memoize_top_down[capacity][max_weigth]


# method to read top the matix and get the selected items
def __get_list_benefits(benefits, weigths, capacity, max_weigth):
    benefits_aux = []
    i = capacity
    k = max_weigth

    while i > 0 and k > 0:
        if memoize_top_down[i][k] != memoize_top_down[i - 1][k]:
            benefits_aux.append(i)
            i = i - 1
            k = k - weigths[i]
        else:
            i = i - 1

    benefits_aux.sort()

    return benefits_aux


def routines_brute_force(total_weight, items_weights, benefits, capacity, iterations):
    for _ in range(int(iterations)):
        included = []

        answer, included = knapsack_brute_force(total_weight, items_weights, benefits, capacity, included)
        print("Beneficio máximo: ", answer)
        print("Incluidos: ", str(included)[1:-1])


def knapsack_brute_force(total_weight, items_weights, benefits, capacity, included):
    if capacity == 0 or total_weight == 0:
        return 0, included

    if items_weights[capacity - 1] > total_weight:
        return knapsack_brute_force(total_weight, items_weights, benefits, capacity - 1, included)

    else:
        sum_1, included_temp1 = knapsack_brute_force(total_weight - items_weights[capacity - 1], items_weights,
                                                     benefits,
                                                     capacity - 1, [capacity] + included)
        sum_1 += benefits[capacity - 1]
        sum_2, included_temp2 = knapsack_brute_force(total_weight, items_weights, benefits, capacity - 1, included)

        if sum_1 > sum_2:
            return sum_1, included_temp1
        else:
            return sum_2, included_temp2
