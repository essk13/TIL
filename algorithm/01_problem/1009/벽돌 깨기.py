import sys
sys.stdin = open('brick.txt', 'r')

from copy import deepcopy

def break_(r, c):
    tg = test[r][c]
    test[r][c] = 0
    cnt = 1
    for i in range(1, tg):
        for j in range(4):
            ny, nx = r + dy[j] * i, c + dx[j] * i
            if 0 <= ny < H and 0 <= nx < W:
                if test[ny][nx] > 1:
                    cnt += break_(ny, nx)
                elif test[ny][nx] == 1:
                    test[ny][nx] = 0
                    cnt += 1
    return cnt


def gravity():
    for y in range(H - 2, -1, -1):
        for x in range(W):
            if test[y][x]:
                idx = 1
                while y+idx < H and test[y+idx][x] == 0:
                    idx += 1
                test[y][x], test[y+idx-1][x] = test[y+idx-1][x], test[y][x]
    return


def ck():
    cnt = 0
    for r in range(H):
        for c in range(W):
            if test[r][c]:
                cnt += 1
    return cnt


def shoot(lv, cnt):
    global min_, test
    if lv == N or cnt == 0:
        min_ = min(min_, cnt)
        return
    origin = deepcopy(test)
    for x in range(W):
        for y in range(H):
            if test[y][x]:
                if y > 0 and test[y-1][x]:
                    break
                break_(y, x)
                cnt = ck()
                gravity()
                shoot(lv + 1, cnt)
                test = deepcopy(origin)
                break


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    test = deepcopy(MAP)
    min_ = 21e8
    cnt = ck()
    shoot(0, cnt)
    print('#{} {}'.format(tc+1, min_))
