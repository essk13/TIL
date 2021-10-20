import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

qu = deque()
cnt = 0
for y in range(N):
    for x in range(M):
        if MAP[y][x] == 0: cnt += 1
        elif MAP[y][x] == 1: qu.append((y, x, 0))

ans = 0
while qu:
    r, c, day = qu.popleft()
    ans = max(ans, day)
    for i in range(4):
        y, x = r + dy[i], c + dx[i]
        if y < 0 or y >= N or x < 0 or x >= M: continue
        if MAP[y][x] == 1 or MAP[y][x] == -1: continue
        MAP[y][x] = 1
        cnt -= 1
        qu.append((y, x, day + 1))

if cnt == 0:
    print(ans)
else:
    print(-1)
