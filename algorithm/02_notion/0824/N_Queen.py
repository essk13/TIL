def check(y, i):
    # j = 0
    # while (y + j) < N and (i + j) < N:
    #     MAP[y + j][i + j] += 1
    #     j += 1
    j = 0
    while (y + j) < N and (i - j) >= 0:
        MAP[y + j][i - j] += 1
        j += 1


def uncheck(y, i):
    # j = 0
    # while (y + j) < N and (i + j) < N:
    #     MAP[y + j][i + j] -= 1
    #     j += 1
    j = 0
    while (y + j) < N and (i - j) >= 0:
        MAP[y + j][i - j] -= 1
        j += 1


def queen(y):
    global cnt
    if y == N:
        cnt += 1
        return
    for i in range(N):
        if MAP[y][i] == 0 and used_x[i] == 0 and (y - i) != 0:
            used_x[i] = 1
            diagonal1[i] = 0
            check(y, i)
            queen(y+1)
            used_x[i] = 0
            diagonal1[i] = -1
            uncheck(y, i)

    return


N = int(input())
MAP = [[0]*N for _ in range(N)]
used_x = [0] * N
diagonal1 = [-1] * N
diagonal2 = [-1] * N
cnt = 0
queen(0)
print(cnt)
