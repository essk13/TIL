import sys
from collections import deque

def ck(r, c):
    cnt = 0
    qu = deque([(MAP[r][c], r, c, [(r, c)], 1, '')])
    while qu:
        total, y, x, visited, lv, d = qu.popleft()
        if lv == 4:
            cnt = max(cnt, total)
            continue
        if lv == 3 and (d == '00' or d == '11' or d == '22' or d =='33'):
            qu.append((total, visited[1][0], visited[1][1], visited, lv, d + '-'))
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (ny, nx) in visited: continue
            if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
            qu.append((total + MAP[ny][nx], ny, nx, visited + [(ny, nx)], lv+1, d + str(i)))
    return cnt


N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ans = 0
for y in range(N):
     for x in range(M):
         ans = max(ans, ck(y, x))

print(ans)