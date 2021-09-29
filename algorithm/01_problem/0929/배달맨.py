import sys
sys.stdin = open('배달.txt', 'r')
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    H, W, N = map(int, input().split())
    MAP = [input() for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    visited[0][0] = 1

    sy, sx = 0, 0
    ans = 0
    for i in range(1, N+1):
        qu = deque([(sy, sx, 0)])
        while qu:
            ny, nx, lv = qu.popleft()
            if MAP[ny][nx] == str(i):
                ans += lv
                sy, sx = ny, nx
                break
            for j in range(4):
                ty, tx = ny + dy[j], nx + dx[j]
                if 0 <= ty < H and 0 <= tx < W:
                    if visited[ty][tx] == i: continue
                    if MAP[ty][tx] == '#': continue
                    visited[ty][tx] = i
                    qu.append((ty, tx, lv+1))

    print('#{} {}'.format(tc+1, ans))
