import sys
sys.stdin = open('등산로.txt', 'r')

from collections import deque

def dig(r, c, dig_t):
    queue = deque([[r, c, 1, dig_t, MAP[r][c], [r, c]]])
    max_lv = 0
    while queue:
        ny, nx, lv, dig, h, visited = queue.popleft()
        max_lv = max(max_lv, lv)
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < N:
                if h > MAP[ty][tx] and [ty, tx] not in visited:
                    queue.append([ty, tx, lv + 1, dig, MAP[ty][tx], visited + [[ty, tx]]])
                if dig:
                    if h <= MAP[ty][tx] and [ty, tx] not in visited:
                        if h > MAP[ty][tx] - K:
                            queue.append([ty, tx, lv+1, 0, MAP[ty][tx] - K, visited + [[ty, tx]]])
    return max_lv


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0
    cnt = 0
    for i in range(N):
        max_h = max(max_h, max(MAP[i]))
        cnt += 1

    ans = 0
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == max_h:
                ans = max(ans, dig(y, x, 1))
    if cnt == 1:
        ret = False
        for y in range(N):
            for x in range(N):
                if MAP[y][x] == max_h:
                    MAP[y][x] -= K
                    ret = True
                    break
            if ret:
                break

    max_h = 0
    for i in range(N):
        max_h = max(max_h, max(MAP[i]))

    for y in range(N):
        for x in range(N):
            if MAP[y][x] == max_h:
                ans = max(ans, dig(y, x, 0))

    print('#{} {}'.format(tc+1, ans))
