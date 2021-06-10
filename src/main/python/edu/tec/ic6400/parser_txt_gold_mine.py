def parser(filename):
    file1 = open(filename, 'r')
    lines = file1.readlines()

    count = 0
    # Strips the newline character
    item_weight = []
    matrix = []
    for line in lines:
        line.strip('\n')
        matrix.append(list(eval(line)))
    m = (len(matrix))
    n = (len(matrix[0]))
    print(matrix)
    return matrix


parser("mina1.txt")
