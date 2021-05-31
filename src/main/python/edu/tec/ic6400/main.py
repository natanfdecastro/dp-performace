
from src.main.python.edu.tec.ic6400.knapsack import *
def main():
    val = [20, 50, 60, 62 , 40]
    wt = [5, 15, 10, 10, 8]
    W = 30
    n = len(val)
    rutinas_brute_force(W, wt, val, n)



main()
