import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check(i, j):
    q = deque([[i, j]])
    wall = []
    res = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc]:
                continue

            visited[nr][nc] = 1
            if MAP[nr][nc]:
                wall.append([nr, nc])
            else:
                q.append([nr, nc])
                res += 1

    for r, c in wall:
        ans[r][c] += res
        visited[r][c] = 0
    return


N, M = map(int, input().split())
MAP = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = [[0] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if MAP[r][c] == 0 and visited[r][c] == 0:
            visited[r][c] = 1
            check(r, c)
        elif MAP[r][c]:
            ans[r][c] += 1

for r in range(N):
    for c in range(M):
        if ans[r][c]:
            ans[r][c] %= 10

for l in range(N):
    print(''.join(map(str, ans[l])))
