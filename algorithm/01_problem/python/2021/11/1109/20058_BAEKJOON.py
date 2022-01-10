import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline


def turn(sy, sx, L):
    ny = sy
    for x in range(sx, sx + (2 ** L)):
        nx = sx
        for y in range(sy + (2 ** L) - 1, sy - 1, -1):
            next_MAP[ny][nx] = MAP[y][x]
            nx += 1
        ny += 1
    return


def part(L):
    nr = nc = 0
    while nr < 2 ** N:
        while nc < 2 ** N:
            turn(nr, nc, L)
            nc += (2 ** L)
        nc = 0
        nr += (2 ** L)
    return


def melt(r, c):
    cnt = 0
    for i in range(4):
        ny, nx = r + dy[i], c + dx[i]
        if ny < 0 or ny >= 2 ** N or nx < 0 or nx >= 2 ** N: continue
        if MAP[ny][nx] == 0: continue
        cnt += 1

    if cnt < 3:
        melting[r][c] += 1
    return


def checking(r, c):
    global max_
    visited[r][c] = 0
    qu = deque([(r, c)])
    cnt = 0
    while qu:
        y, x = qu.popleft()
        cnt += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= 2 ** N or nx < 0 or nx >= 2 ** N: continue
            if visited[ny][nx] and MAP[ny][nx]:
                visited[ny][nx] = 0
                qu.append((ny, nx))
    max_ = max(cnt, max_)
    return


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, Q = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(2 ** N)]
fire = list(map(int, input().split()))

for rank in fire:
    next_MAP = [[0] * (2 ** N) for _ in range(2 ** N)]
    # 필드 회전
    part(rank)
    MAP = deepcopy(next_MAP)

    # 얼음 녹이기
    melting = [[0] * (2 ** N) for _ in range(2 ** N)]
    for y in range(2 ** N):
        for x in range(2 ** N):
            if MAP[y][x]:
                melt(y, x)

    for y in range(2 ** N):
        for x in range(2 ** N):
            MAP[y][x] -= melting[y][x]

# 답 계산
ans = max_ = 0
visited = [[1] * (2 ** N) for _ in range(2 ** N)]
for y in range(2 ** N):
    for x in range(2 ** N):
        if MAP[y][x] and visited[y][x]:
            checking(y, x)

for y in range(2 ** N):
    ans += sum(MAP[y])

print(ans)
print(max_)
