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


# Matrix use to memoization of top down approach
memoize_top_down = []
# values setter for knapsack with top down approach
def knapsack_top_down(max_weigth, weigths, benefits, n, iterations):

    memo = [[0 for i in range(max_weigth + 1)] for j in range(n + 1)]
    
    for i in memo:
        memoize_top_down.append(i)

    for i in range(int(iterations)):
        print("Beneficio Maximo: ", __knapsack(weigths, benefits, max_weigth, n))
        print("Incluidos: ", __get_list_benefits(benefits, weigths, n, max_weigth))

# knapsack with top down approach
def __knapsack(wtf, vals, wf, nf):

    # base conditions
    if nf == 0 or wf == 0:
        return 0
    if memoize_top_down[nf][wf] != 0:
        return memoize_top_down[nf][wf]

    # choice diagram code
    if wtf[nf - 1] <= wf:
        memoize_top_down[nf][wf] = max(vals[nf - 1] + __knapsack(wtf, vals, wf - wtf[nf - 1], nf - 1), __knapsack(wtf, vals, wf, nf - 1))
        return memoize_top_down[nf][wf]

    elif wtf[nf - 1] > wf:
        memoize_top_down[nf][wf] = __knapsack(wtf, vals, wf, nf - 1)
        return memoize_top_down[nf][wf]

# method to read top the matix and get the selected items
def __get_list_benefits(val,wt,n,W):
    benefits = []
    i = n
    k = W

    while i > 0 and k > 0:
        if memoize_top_down[i][k] != memoize_top_down[i - 1][k]:
            benefits.append([i,val[i - 1],wt[i-1]])
            i = i - 1
            k = k - wt[i]
        else:
            i = i - 1
    return benefits



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
