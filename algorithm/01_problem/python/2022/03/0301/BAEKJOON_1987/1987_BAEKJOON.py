import sys
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(r, c, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
        o = ord(MAP[nr][nc])
        if used[o]: continue

        stop = False
        used[o] = 1
        move(nr, nc, cnt + 1)
        used[o] = 0
    return


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

alpha = list(range(ord("A"), ord("Z") + 1))
state = [0] * 26
used = dict(zip(alpha, state))
used[ord(MAP[0][0])] = 1

ans = 0
move(0, 0, 1)
print(ans)
