
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
    matrix=[]
    for line in Lines:
        print (line)
        line.strip('\n')
        matrix.append(list(eval(line)))
    m=(len(matrix))
    n=(len(matrix[0]))
    print(matrix)
    return matrix


parser("mina1.txt")


