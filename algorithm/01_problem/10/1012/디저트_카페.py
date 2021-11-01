import sys
sys.stdin = open('tour.txt', 'r')

def tour(r, c, lv, d):
    global max_
    if (r, c) == (y, x) and lv != 0 and lv != 1:
        max_ = max(max_, lv)
        return
    ny, nx = r + dy[d], c + dx[d]
    if 0 <= ny < N and 0 <= nx < N:
        if eat[MAP[ny][nx]] == 0 and vi[ny][nx] == 0:
            vi[ny][nx] = 1
            eat[MAP[ny][nx]] = 1
            tour(ny, nx, lv+1 ,d)
            vi[ny][nx] = 0
            eat[MAP[ny][nx]] = 0

    if d < 3:
        d += 1
        ny, nx = r + dy[d], c + dx[d]
        if 0 <= ny < N and 0 <= nx < N:
            if eat[MAP[ny][nx]] == 0 and vi[ny][nx] == 0:
                vi[ny][nx] = 1
                eat[MAP[ny][nx]] = 1
                tour(ny, nx, lv + 1, d)
                vi[ny][nx] = 0
                eat[MAP[ny][nx]] = 0
    return


dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    vi = [[0] * N for _ in range(N)]
    eat = [0] * 101

    max_ = -1
    for y in range(N):
        for x in range(N):
            tour(y, x, 0, 0)
            eat = [0] * 101
    print('#{} {}'.format(tc+1, max_))