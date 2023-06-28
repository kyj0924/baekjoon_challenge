N, M = map(int, input().split())
board_in_list = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        board_in_list[i][j] = temp[j]
w_nmlist = [[0 for i in range(8)] for j in range(8)]
for row in range(1, 9, 1):
    for col in range(1, 9, 1):
        if row % 2 != 0:
            if col % 2 != 0:
                w_nmlist[row - 1][col - 1] = 'W'
            else:
                w_nmlist[row - 1][col - 1] = 'B'
        else:
            if col % 2 != 0:
                w_nmlist[row - 1][col - 1] = 'B'
            else:
                w_nmlist[row - 1][col - 1] = 'W'
min_count = 100
w_count = 0
b_count = 0
for i in range(0, N-8 + 1, 1):
    for j in range(0, M-8 + 1, 1):
        w_count = 0
        b_count = 0
        for row in range(0, 8, 1):
            for col in range(0, 8, 1):
                if board_in_list[row + i][col + j] != w_nmlist[row][col]:
                    w_count += 1
        for row in range(0, 8, 1):
            for col in range(0, 8, 1):
                if board_in_list[row + i][col + j] == w_nmlist[row][col]:
                    b_count += 1
        if min_count > w_count:
            min_count = w_count
        if min_count > b_count:
            min_count = b_count

print(min_count)