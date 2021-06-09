
"""
function that is responsible for parse
 the text and converts the input into a matrix
 with the weight of the knapsack, benefits for items and weights for items
"""
def parser(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    item_weight=[]
    item_benefit=[]
    for line in Lines:
        if count==0:
            knapsack_weight=[int(line.rstrip())]
            count+=1
        partitioned_string = line.partition(',')
        split_weight= partitioned_string[0]
        split_benefit = partitioned_string[2]
        if(split_benefit!=""):
            item_benefit.append(int(split_benefit.rstrip()))
            item_weight.append(int(split_weight.rstrip()))
    matrix_result_parse=[knapsack_weight,item_benefit,item_weight]
    return matrix_result_parse


