import sys
sys.stdin = open('room.txt', 'r')
from collections import deque

def check(y, x, lv, start):
    qu = deque([[y, x, lv, start]])
    while qu:
        r, c, nlv, st = qu.popleft()
        for i in range(4):
            ny, nx = r + dy[i], c + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if MAP[r][c] + 1 == MAP[ny][nx]:
                    qu.append([ny, nx, nlv+1, start])
    return (nlv, st)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    path = 0
    st = 21e8
    for i in range(N):
        for j in range(N):
            res = check(i, j, 1, MAP[i][j])
            if res[0] == path:
                st = min(st, res[1])
            elif res[0] > path:
                path = max(path, res[0])
                st = res[1]
    print('#{} {} {}'.format(tc+1, st, path))
