import sys
I = sys.stdin.readline
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def find(r, c):
    q = deque([(r, c)])
    color = MAP[r][c]
    target = []
    rb = []
    while q:
        y, x = q.popleft()
        target.append((y, x))
        if MAP[y][x] == 0:
            rb.append((y, x))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
            if MAP[ny][nx] != 0 and MAP[ny][nx] != color: continue
            if visited[ny][nx]: continue

            visited[ny][nx] = 1
            q.append((ny, nx))

    for y, x in rb:
        visited[y][x] = 0

    return target, len(target), len(rb)


def remove():
    for y, x in tg:
        MAP[y][x] = -2
    return cnt ** 2


def gravity():
    for y in range(N-2, -1, -1):
        for x in range(N-1, -1, -1):
            if MAP[y][x] == -1 or MAP[y][x] == -2: continue

            g = 0
            while y+(g+1) != N and MAP[y+(g+1)][x] == -2:
                g += 1
            MAP[y][x], MAP[y+g][x] = MAP[y+g][x], MAP[y][x]
    return


def turn():
    chg_MAP = []
    for x in range(N-1, -1, -1):
        new_line = []
        for y in range(N):
            new_line.append(MAP[y][x])
        chg_MAP.append(new_line)
    return chg_MAP


N, M = map(int, I().split())
MAP = [list(map(int, I().split())) for _ in range(N)]
ans = 0
while True:
    visited = [[0] * N for _ in range(N)]
    tg = []
    rainbow = 0
    cnt = 0
    for y in range(N):
        for x in range(N):
            if MAP[y][x] <= 0 or visited[y][x]: continue

            visited[y][x] = 1
            tg_lst, tg_cnt, rb = find(y, x)

            if tg_cnt == cnt:
                if rb >= rainbow:
                    tg = tg_lst
                    cnt = tg_cnt
                    rainbow = rb

            elif tg_cnt > cnt:
                tg = tg_lst
                cnt = tg_cnt
                rainbow = rb

    if cnt <= 1: break

    ans += remove()
    gravity()
    MAP = turn()
    gravity()

print(ans)
