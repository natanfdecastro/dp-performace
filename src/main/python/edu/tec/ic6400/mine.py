import sys
from sys import path
import random
import gold_mine
import parser_txt_gold_mine

path.append('src.main.python.edu.tec.ic6400')


mode = sys.argv[2]

if mode == "-p":
    print("Se quiere hacer del modo aleatorio")
    algorithm = int(sys.argv[1])
    N = int(sys.argv[3])
    M = int(sys.argv[4])
    min = int(sys.argv[5])
    max = int(sys.argv[6])
    iterations = int(sys.argv[7])
    random_matrix = []
    random_list = []
    for i in range(0, N):
        random_list = []
        for j in range(0, M):
            random_list.append(random.choice(range(min, max)))
        random_matrix.append(random_list)
    print(random_matrix)
    if algorithm == 1:
        pass
    elif algorithm == 2:
        print('11')


elif mode == "-a":
    print("Se quiere hacer del modo manual")
    algorithm = sys.argv[1]
    file = sys.argv[3]
    iterations = sys.argv[4]
    gold_matrix = parser_txt_gold_mine.parser(file)
    n = len(gold_matrix)
    m = len(gold_matrix[0])
    if algorithm == 1:
        pass
    elif algorithm == "2":
        gold_mine.gold_mine_dp(gold_matrix,n,m)
    else:
        pass
