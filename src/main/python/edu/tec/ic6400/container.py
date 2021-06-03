import sys
from sys import path
path.append('src.main.python.edu.tec.ic6400')
import knapsack


# total arguments
mode=sys.argv[2]

if(mode=="-p"):
    print("Se quiere hacer del modo aleatorio")
    algorithm=sys.argv[1]
    weight=sys.argv[3]
    number_of_elements=sys.argv[4]
    weight_range=sys.argv[5]
    range_Benefits=sys.argv[6]
    iterations=sys.argv[7]
    print(algorithm,weight,number_of_elements,weight_range,range_Benefits,iterations)

elif(mode=="-a"):
    print("Se quiere hacer del modo manual")
    algorithm=sys.argv[1]
    file=sys.argv[3]
    iterations=sys.argv[4]
    if(algorithm=="1"):
        knapsack.routines_brute_force(file,iterations)

