import sys
from collections import deque
I = sys.stdin.readline

def Union(r, c):
    cnt = 0
    qu = deque([(r, c)])
    union[r][c] = n
    while qu:
        y, x = qu.popleft()
        total[n] += world[y][x]
        cnt += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
            if L <= abs(world[y][x] - world[ny][nx]) <= R and union[ny][nx] == 0:
                union[ny][nx] = n
                qu.append((ny, nx))
    un[n] = cnt
    return cnt


N, L, R = map(int, I().split())
world = [list(map(int, I().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

day = 0
while True:
    union = [[0] * N for _ in range(N)]
    un = [0] * (N ** 2 + 1)
    total = [0] * (N ** 2 + 1)
    n = 1
    con = 1
    now = 0
    for y in range(N):
        for x in range(N):
            if union[y][x] == 0:
                cnt = Union(y, x)
                con = max(con, cnt)
                n += 1
                now += cnt
                if now == N ** 2: break
        if now == N ** 2: break
    if con == 1: break

    day += 1
    for y in range(N):
        for x in range(N):
            world[y][x] = total[union[y][x]] // un[union[y][x]]

print(day)
