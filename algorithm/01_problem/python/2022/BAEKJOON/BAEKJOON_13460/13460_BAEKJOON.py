import sys
from copy import deepcopy
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(di, e, ball, br, bc):
    m = 0
    if MAP[br][bc] == 'O':
        return 0

    mr, mc = br, bc
    while True:
        nr, nc = mr + dr[di], mc + dc[di]
        if MAP[nr][nc] == '.' and [nr, nc] != e:
            mr, mc = nr, nc
            m += 1
            continue
        elif MAP[nr][nc] == 'O':
            ball[0] = nr
            ball[1] = nc
            return -1
        else:
            break

    ball[0] = mr
    ball[1] = mc
    return m


def play(pre, cnt):
    if cnt == 10:
        return

    pr[cnt] = deepcopy(red)
    pb[cnt] = deepcopy(blue)
    for d in range(4):
        red[0], red[1] = pr[cnt][0], pr[cnt][1]
        blue[0], blue[1] = pb[cnt][0], pb[cnt][1]
        if cnt and d == pre:
            continue

        stop = 0
        while True:
            res_r = move(d, blue, red, red[0], red[1])
            res_b = move(d, red, blue, blue[0], blue[1])
            res_r += move(d, blue, red, red[0], red[1])

            if res_r == 0 and res_b == 0:
                break

            elif res_r == -1 and res_b != -1:
                global ans
                ans = min(cnt + 1, ans)
                stop = 1
                break

            elif res_b == -1:
                stop = 1
                break

        if stop:
            continue
        play(d, cnt + 1)
    return


N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]

red = []
blue = []
for r in range(N):
    for c in range(M):
        if MAP[r][c] == 'R':
            MAP[r][c] = '.'
            red = [r, c]
        elif MAP[r][c] == 'B':
            MAP[r][c] = '.'
            blue = [r, c]

pr = [[] for _ in range(10)]
pb = [[] for _ in range(10)]
ans = 11
play(-1, 0)
if ans == 11:
    print(-1)
else:
    print(ans)
