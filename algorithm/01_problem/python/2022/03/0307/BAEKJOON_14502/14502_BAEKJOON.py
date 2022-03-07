import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check():
    visited = [[0] * M for _ in range(N)]
    q = deque(virus)
    res = cnt
    for i, j in q:
        visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for d in range(4):
            nr, nc = i + dr[d], j + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if visited[nr][nc] or MAP[nr][nc]: continue

            visited[nr][nc] = 1
            q.append([nr, nc])
            res -= 1
            if res <= ans:
                return 0

    return res


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

virus = []
cnt = -3
for r in range(N):
    for c in range(M):
        if MAP[r][c] == 2:
            virus.append([r, c])
        elif MAP[r][c] == 0:
            cnt += 1

ans = 0
for x in range(N * M):
    xr, xc = x // M, x % M
    if MAP[xr][xc]: continue
    MAP[xr][xc] = 1
    for y in range(x + 1, N * M):
        yr, yc = y // M, y % M
        if MAP[yr][yc]: continue
        MAP[yr][yc] = 1
        for z in range(y + 1, N * M):
            zr, zc = z // M, z % M
            if MAP[zr][zc]: continue
            MAP[zr][zc] = 1
            ans = max(ans, check())
            MAP[zr][zc] = 0
        MAP[yr][yc] = 0
    MAP[xr][xc] = 0

print(ans)
