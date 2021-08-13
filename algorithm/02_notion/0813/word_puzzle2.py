def is_row(y, x, k):
    if x + k < N and MAP[y][x+k] == 1: return 0
    if x - 1 > 0 and MAP[y][x-1] == 1: return 0
    if x + k - 1 >= N: return  0

    for i in range(k):
        if MAP[y][x+i] == 0:
            return 0

    return 1


def is_column(y, x, k):
    if y + k < N and MAP[y+1][x] == 1: return 0
    if y - 1 > 0 and MAP[y-1][x] == 1: return 0
    if y + K -1 >= N: return 0

    for i in range(K):
        if MAP[y+i][x] == 0:
            return 0

    return 1


N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for y in range(N):
    for x in range(N):
        cnt += is_row(y, x, K)
        cnt += is_column(y, x, K)

print(cnt)