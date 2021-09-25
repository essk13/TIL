import sys
sys.stdin = open('등산로.txt', 'r')
# from collections import deque

# def bfs(r, c):
#     queue = deque([[r, c, 1, MAP[r][c], [r, c], 1]])
#     max_lv = 0
#     while queue:
#         ny, nx, dig, h, visit, lv = queue.popleft()
#         max_lv = max(max_lv, lv)
#         for i in range(4):
#             ty, tx = ny + dy[i], nx + dx[i]
#             if 0 <= ty < N and 0 <= tx < N:
#                 if MAP[ty][tx] < h and [ty, tx] not in visit:
#                     queue.append([ty, tx, dig, MAP[ty][tx], visit + [[ty, tx]], lv + 1])
#                 if dig:
#                     if MAP[ty][tx] >= h and [ty, tx] not in visit:
#                         if MAP[ty][tx] - K < h:
#                             for j in range(1, K+1):
#                                 queue.append([ty, tx, 0, h - j, visit + [[ty, tx]], lv + 1])
#     return max_lv


def dfs(r, c, lv, dig, h):
    global ans
    ans = max(ans, lv)
    for i in range(4):
        ny, nx = r + dy[i], c + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if visited[ny][nx] == 0:
                if MAP[ny][nx] < h:
                    visited[ny][nx] = 1
                    dfs(ny, nx, lv + 1, dig, MAP[ny][nx])
                    visited[ny][nx] = 0
                elif dig and MAP[ny][nx] - K < h:
                    visited[ny][nx] = 1
                    dfs(ny, nx, lv + 1, 0, h - 1)
                    visited[ny][nx] = 0
    return

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
                visited[y][x] = 1
                dfs(y, x, 1, 1, MAP[y][x])
                visited[y][x] = 0

    print('#{} {}'.format(tc+1, ans))
