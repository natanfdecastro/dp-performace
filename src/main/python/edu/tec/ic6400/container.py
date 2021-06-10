import sys
from sys import path
import knapsack
import random
import parser_txt_knapsack

path.append('src.main.python.edu.tec.ic6400')

# total arguments
mode = sys.argv[2]

if mode == "-p":

    print("[ Random Mode ]")

    algorithm = sys.argv[1]
    weight = sys.argv[3]
    number_of_elements = sys.argv[4]
    weight_range = sys.argv[5]
    benefits_range = sys.argv[6]

    # A split is done to separate the numbers and make the range
    partitioned_string = weight_range.partition('-')
    weight_range_1 = partitioned_string[0]
    weight_range_2 = partitioned_string[2]
    partitioned_string = benefits_range.partition('-')
    benefits_range_1 = partitioned_string[0]
    benefits_range_2 = partitioned_string[2]
    iterations = sys.argv[7]

    # join the numbers and save the range
    benefits_range = (range(int(benefits_range_1), int(benefits_range_2)))
    weight_range = (range(int(weight_range_1), int(weight_range_2)))
    benefits_range_list = []
    weight_range_list = []

    # the list of numbers is stored in lists
    for i in benefits_range:
        benefits_range_list.append(i)

    for i in weight_range:
        weight_range_list.append(i)

    # make a random (they mess up) the numbers of the lists to carry out the random
    random.shuffle(benefits_range_list)
    random.shuffle(weight_range_list)

    item_weight = []
    item_benefit = []

    for i in range(int(number_of_elements)):
        item_benefit.append(random.choice(benefits_range_list))
        item_weight.append(random.choice(weight_range_list))

    if algorithm == "1":
        knapsack.routines_brute_force(int(weight), item_weight, item_benefit, int(number_of_elements), int(iterations))
    elif algorithm == "2":
        knapsack.knapsack_bottom_up(int(weight), item_weight, item_benefit, int(number_of_elements), int(iterations))


elif mode == "-a":

    print("[ Manual Mode ]")
    algorithm = sys.argv[1]
    file = sys.argv[3]
    iterations = sys.argv[4]

    matrix_result = parser_txt_knapsack.parser(file)

    total_weight = matrix_result[0][0]
    items_weights = matrix_result[2]
    benefits = matrix_result[1]
    capacity = len(matrix_result[1])

    if algorithm == "1":
        knapsack.routines_brute_force(total_weight, items_weights, benefits, capacity, iterations)
    elif algorithm == "2":
        knapsack.knapsack_bottom_up(total_weight, items_weights, benefits, capacity, iterations)
    elif(algorithm=="3"):
        knapsack.knapsack_top_down(total_weight, items_weights, benefits, capacity,iterations)
