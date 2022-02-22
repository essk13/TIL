import sys
from copy import deepcopy
input = sys.stdin.readline


def up():
    visited = [[0] * N for _ in range(N)]
    for c in range(N):
        for r in range(N):
            if MAP[r][c] == 0: continue
            val = MAP[r][c]
            MAP[r][c] = 0

            nr = r
            while nr > 0 and MAP[nr-1][c] == 0:
                nr -= 1
            if nr > 0 and MAP[nr-1][c] == val and visited[nr-1][c] == 0:
                MAP[nr-1][c] *= 2
                visited[nr-1][c] = 1
            else:
                MAP[nr][c] = val
    return


def down():
    visited = [[0] * N for _ in range(N)]
    for c in range(N):
        for r in range(N-1, -1, -1):
            if MAP[r][c] == 0: continue
            val = MAP[r][c]
            MAP[r][c] = 0

            nr = r
            while nr < N - 1 and MAP[nr+1][c] == 0:
                nr += 1
            if nr + 1 < N and MAP[nr+1][c] == val and visited[nr+1][c] == 0:
                MAP[nr+1][c] *= 2
                visited[nr+1][c] = 1
            else:
                MAP[nr][c] = val
    return


def left():
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 0: continue
            val = MAP[r][c]
            MAP[r][c] = 0

            nc = c
            while nc > 0 and MAP[r][nc-1] == 0:
                nc -= 1
            if nc > 0 and MAP[r][nc-1] == val and visited[r][nc-1] == 0:
                MAP[r][nc-1] *= 2
                visited[r][nc-1] = 1
            else:
                MAP[r][nc] = val
    return


def right():
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N-1, -1, -1):
            if MAP[r][c] == 0: continue
            val = MAP[r][c]
            MAP[r][c] = 0

            nc = c
            while nc < N - 1 and MAP[r][nc + 1] == 0:
                nc += 1
            if nc + 1 < N and MAP[r][nc + 1] == val and visited[r][nc + 1] == 0:
                MAP[r][nc + 1] *= 2
                visited[r][nc + 1] = 1
            else:
                MAP[r][nc] = val
    return


def move(cnt):
    global ans, MAP
    if cnt == 5:
        for r in range(N):
            for c in range(N):
                ans = max(MAP[r][c], ans)
        return

    up()
    maps[cnt+1] = deepcopy(MAP)
    move(cnt + 1)
    MAP = deepcopy(maps[cnt])
    maps[cnt + 1] = deepcopy(MAP)
    down()
    maps[cnt + 1] = deepcopy(MAP)
    move(cnt + 1)
    MAP = deepcopy(maps[cnt])
    left()
    maps[cnt + 1] = deepcopy(MAP)
    move(cnt + 1)
    MAP = deepcopy(maps[cnt])
    right()
    maps[cnt + 1] = deepcopy(MAP)
    move(cnt + 1)
    MAP = deepcopy(maps[cnt])
    return


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
maps = [deepcopy(MAP) for _ in range(6)]
ans = 0
move(0)
print(ans)
