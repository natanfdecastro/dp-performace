import sys
from sys import path
path.append('src.main.python.edu.tec.ic6400')
import knapsack
import random



mode=sys.argv[2]

if(mode=="-p"):
    print("Se quiere hacer del modo aleatorio")

    algorithm=sys.argv[1]
    weight=sys.argv[3]
    number_of_elements=sys.argv[4]
    weight_range=sys.argv[5]
    benefits_range=sys.argv[6]

    #Se hace un split para separar los numeros y hacer el rango
    partitioned_string = weight_range.partition('-')
    weight_range_1= partitioned_string[0]
    weight_range_2 = partitioned_string[2]
    partitioned_string = benefits_range.partition('-')
    benefits_range_1= partitioned_string[0]
    benefits_range_2 = partitioned_string[2]
    iterations=sys.argv[7]

    #se junta los numeros y se guarda el rango
    benefits_range=(range(int(benefits_range_1),int(benefits_range_2)))
    weight_range=(range(int(weight_range_1),int(weight_range_2)))
    benefits_range_list=[]
    weight_range_list=[]

    #se almacena la lista de numeros en listas
    for i in benefits_range:
        benefits_range_list.append(i)

    for i in weight_range:
        weight_range_list.append(i)

    #se hace un random(desordenan) los numeros de las listas para efectuar el aleatorio
    random.shuffle(benefits_range_list)
    random.shuffle(weight_range_list)

   # print(benefits_range_list)
   # print(weight_range_list)
    item_weight=[]
    item_benefit=[]

    for i in range(int(number_of_elements)):
        item_benefit.append(random.choice(benefits_range_list))
        item_weight.append(random.choice(weight_range_list))


    print(item_benefit)
    print(item_weight)
    knapsack.routines_brute_force_random(int(weight),item_weight,item_benefit,int(number_of_elements),int(iterations))
   # print(algorithm,weight,number_of_elements,weight_range,benefits_ran
# ge,iterations)

elif(mode=="-a"):
    print("Se quiere hacer del modo manual")
    algorithm=sys.argv[1]
    file=sys.argv[3]
    iterations=sys.argv[4]
    if(algorithm=="1"):
        knapsack.routines_brute_force(file,iterations)

