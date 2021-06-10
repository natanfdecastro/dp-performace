def gold_mine_dp(gold, m, n):
    goldTable = [[0 for i in range(n)]
                 for j in range(m)]

    for col in range(n - 1, -1, -1):
        for row in range(m):

            # Check de value on the rigth cell (->)
            if (col == n - 1):
                right = 0
            else:
                right = goldTable[row][col + 1]

            #  Check de value on the right up cell (/)
            if (row == 0 or col == n - 1):
                right_up = 0
            else:
                right_up = goldTable[row - 1][col + 1]

            #  Check de value on the right_down cell
            if (row == m - 1 or col == n - 1):
                right_down = 0
            else:
                right_down = goldTable[row + 1][col + 1]

            # Save the max gold collected from taking either of the above 3 paths
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down)

    answer = goldTable[0][0]
    for i in range(m):
        answer = max(answer, goldTable[i][0])

    print("El maximo de oro a recolectar es: ",answer)
    print("El camino para recolectar el oro es: ",get_path(goldTable, answer, n, m))



def get_path(goldTable, ans, n, m):
    path = []
    # for to get the bigger value in gold table
    for i in range(0, m):
        if ans == goldTable[i][0]:
            row = i
            for col in range(m):
                # get value in right direction
                if (col == n - 1):
                    right = 0
                else:
                    right = goldTable[row][col + 1]

                # get value in right_up direction
                if (row == 0 or col == n - 1):
                    right_up = 0
                else:
                    right_up = goldTable[row - 1][col + 1]

                # get value in right_down direction
                if (row == m - 1 or col == n - 1):
                    right_down = 0
                else:
                    right_down = goldTable[row + 1][col + 1]

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

