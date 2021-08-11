N = int(input())
# snail = [[0]*(N+2) for _ in range(N+2)]
#
# for i in range(N+2):
#     for j in [0, -1]:
#         snail[j] = [-1] * (N+2)
#         snail[i][j] = -1
#
snail = [[-1]*(N+2) for _ in range(N+2)]
num = 1

for y in range(1, N+1):
    for x in range(1, N+1):
        snail[y][x] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = y = 0
i = 0
while num <= N*N:
    if snail[y+dy[i]][x+dx[i]] == 0:
        x += dx[i]
        y += dy[i]
        snail[x][y] = num
        num += 1
    elif snail[y][x] != -1:
        i += 1
        if i > 3:
            i = 0

for i in range(1,N+1):
    for y in range(1,N+1):
        print(snail[y][x], end=' ')
    print()