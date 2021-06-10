from datetime import datetime


def brute_force(gold_mine, m, n, iterations):

    for k in range(int(iterations)):
        print("[ Iteration: ", k, " ]")
        start_time = datetime.now()

        max_gold = 0
        max_path = []
        path = []
        for i in range(n):
            g, path = gold_mine_recu(i, 0, m, n, path, gold_mine)
            if g > max_gold:
                max_gold = g
                max_path = path
                path = []
        print("Máxima cantidad de oro: ", max_gold)
        # print(max_path[::-1])

        path_i = len(max_path) - 1
        print("Selección de casillas: ", end=" ")
        while path_i >= 0:
            if path_i >= 1:
                print("(", max_path[path_i][0], ",", max_path[path_i][1], ") -> ", end=" ")
            else:
                print("(", max_path[path_i][0], ", ", max_path[path_i][1], ")")
            path_i -= 1

        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print("\n")


def gold_mine_recu(row, col, m, n, path, gold_mine):

    if col >= m:
        return 0, path
    if row >= n or row <= 0:
        return 0, path

    right_up, path_1 = gold_mine_recu(row - 1, col + 1, m, n, path, gold_mine)
    right, path_2 = gold_mine_recu(row, col + 1, m, n, path, gold_mine)
    right_down, path_3 = gold_mine_recu(row + 1, col + 1, m, n, path, gold_mine)

    # print('rigth: ', right, ' n: ', row, ' m: ', col + 1)
    # print('rigth_up: ', right_up, ' n: ', row - 1, ' n: ', col + 1)
    # print('rigth_down: ', right_down, ' n: ', row + 1, ' m: ', col + 1)
    # print("\n")

    right_up += gold_mine[row][col]
    right_down += gold_mine[row][col]
    right += gold_mine[row][col]

    if right_up >= right and right_up >= right_down:
        return right_up, path_1 + [[row, col]]

    elif right >= right_up and right >= right_down:
        return right, path_2 + [[row, col]]

    elif right_down >= right_up and right_down >= right:
        return right_down, path_3 + [[row, col]]


def gold_mine_dp(gold, m, n, iterations):
    print("")
    for i in range(int(iterations)):
        print("[ Iteration: ", i, " ]")
        start_time = datetime.now()
        gold_table = [[0 for i in range(n)]
                     for j in range(m)]

        for col in range(n - 1, -1, -1):
            for row in range(m):

                # Check de value on the rigth cell (->)
                if col == n - 1:
                    right = 0
                else:
                    right = gold_table[row][col + 1]

                #  Check de value on the right up cell (/)
                if row == 0 or col == n - 1:
                    right_up = 0
                else:
                    right_up = gold_table[row - 1][col + 1]

                #  Check de value on the right_down cell
                if row == m - 1 or col == n - 1:
                    right_down = 0
                else:
                    right_down = gold_table[row + 1][col + 1]

                # Save the max gold collected from taking either of the above 3 paths
                gold_table[row][col] = gold[row][col] + max(right, right_up, right_down)

        answer = gold_table[0][0]
        for i in range(m):
            answer = max(answer, gold_table[i][0])

        print("Máximo de oro a recolectar es: ", answer)
        print("Camino para recolectar el oro es: ", get_path(gold_table, answer, n, m))
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print("\n")


def get_path(gold_table, ans, n, m):
    path = []
    # for to get the bigger value in gold table
    for i in range(0, m):
        if ans == gold_table[i][0]:
            row = i
            for col in range(m):
                # get value in right direction
                if col == n - 1:
                    right = 0
                else:
                    right = gold_table[row][col + 1]

                # get value in right_up direction
                if row == 0 or col == n - 1:
                    right_up = 0
                else:
                    right_up = gold_table[row - 1][col + 1]

                # get value in right_down direction
                if row == m - 1 or col == n - 1:
                    right_down = 0
                else:
                    right_down = gold_table[row + 1][col + 1]

                dir_path = max(right, right_up, right_down)

                if right == dir_path:
                    path.append([row, col])
                elif right_up == dir_path:
                    path.append([row, col])
                    row -= 1
                elif right_down == dir_path:
                    path.append([row, col])
                    row += 1
    ans_path = ''
    for index in range(len(path) - 1):
        ans_path += str(path[index]) + '->'

    ans_path += str(path[len(path) - 1])
    return ans_path


def gold_mine_brute_force():
    print("parse")
