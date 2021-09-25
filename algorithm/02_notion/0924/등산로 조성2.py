import sys
sys.stdin = open('등산로.txt', 'r')
from collections import deque

def bfs(r, c):
    queue = deque([[r, c, 1, MAP[r][c], [r, c], 1]])
    max_lv = 0
    while queue:
        ny, nx, dig, h, visit, lv = queue.popleft()
        max_lv = max(max_lv, lv)
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < N:
                if [ty, tx] not in visit:
                    if MAP[ty][tx] < h:
                        queue.append([ty, tx, dig, MAP[ty][tx], visit + [[ty, tx]], lv + 1])
                    elif dig and MAP[ty][tx] - K < h:
                        queue.append([ty, tx, 0, h - 1, visit + [[ty, tx]], lv + 1])
    return max_lv

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_h = 0
    for i in range(N):
        max_h = max(max_h, max(MAP[i]))

    ans = 0
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == max_h:
                ans = max(ans, bfs(y, x))

    print('#{} {}'.format(tc+1, ans))
