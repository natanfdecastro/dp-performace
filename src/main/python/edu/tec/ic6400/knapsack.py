
from sys import path
path.append('src.main.python.edu.tec.ic6400')
import parser_txt_knapsack



def knapsack_bottom_up():
    print("Bottom up")


def knapsack_top_down():
    print("top down")






#call routines to solve the problem with brute force.
def routines_brute_force(fileName,iterations):
    for i in range(int(iterations)):
        matrix_result=parser_txt_knapsack.parser(fileName)
        res=knapsack_brute_force(matrix_result[0][0], matrix_result[2], matrix_result[1], len(matrix_result[1]))
        print("Beneficio máximo: ",res)
        subset_sum(matrix_result[1],res,matrix_result[1])


#call routines to solve the problem with brute force.
def routines_brute_force_random( W, wt, val, n,iterations):


    for i in range(int(iterations)):
        print(i)
        res=knapsack_brute_force(W, wt, val, n)
        print("Beneficio máximo: ",res)
        subset_sum(val, res, val)



#Solve the knapsack problem with the brute force algorithm.
def knapsack_brute_force( W, wt, val, n):
   # initial conditions
   if n == 0 or W == 0 :
      return 0
   # If weight is higher than capacity then it is not included
   if (wt[n-1] > W):
      return knapsack_brute_force(W, wt, val, n-1)
   # return either nth item being included or not
   else:
      return max(val[n-1] + knapsack_brute_force(W-wt[n-1], wt, val, n-1),
         knapsack_brute_force(W, wt, val, n-1))


#Find a subarray with a given sum in an array
def subset_sum(numbers, target,val, partial=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target:
        res= []
        for i in range(len(partial)):
            try:
                res.append(val.index(partial[i])+1)
            except:
                pass
        print("Incluidos: ", res)
        return (res)
    if s >= target:
        return  # if we reach the number why bother to continue
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target,val, partial + [n])



