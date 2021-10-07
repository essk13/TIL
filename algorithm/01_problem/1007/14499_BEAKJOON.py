def turn(cmd):
    global d1, d2, d3, d4
    if cmd == 1:
        d1, d2, d3, d4 = d4, d3, d1, d2
    elif cmd == 2:
        d1, d2, d3, d4 = d3, d4, d2, d1
    return

N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dice = [[0] * 3 for _ in range(4)]
dix = 3
diy = 1
d1, d2, d3, d4 = 1, 2, 3, 4
a = {d1: (1, 2), d2: (1, 0), d3: (3, 1), d4: (1, 1), 5: (2, 1)}
b = {d1: (1, 1), d2: (3, 1), d3: (0, 1), d4: (2, 1), 5: (1, 2)}
c = {d1: (1, 2), d2: (1, 0), d3: (0, 1), d4: (2, 1), 5: (3, 1)}
d = {d1: (3, 1), d2: (1, 1), d3: (0, 1), d4: (2, 1), 5: (1, 0)}
e = {d1: (1, 2), d2: (1, 0), d3: (1, 1), d4: (3, 1), 5: (0, 1)}
f = {d1: (1, 2), d2: (1, 0), d3: (2, 1), d4: (0, 1), 5: (1, 1)}

dixy = {
    (0, 1): a,
    (1, 0): b,
    (1, 1): c,
    (1, 2): d,
    (2, 1): e,
    (3, 1): f,
}

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n = 1
cmds = list(map(int, input().split()))
for cmd in cmds:
    x, y = x + dx[cmd], y + dy[cmd]
    if x < 0 or N <= x or y < 0 or M <= y: continue
    n_dix, n_diy = dixy[(dix, diy)][cmd]
    dix, diy = n_dix, n_diy
    if MAP[x][y] != 0:
        dice[dix][diy] = MAP[x][y]
        MAP[x][y] = 0
    elif MAP[x][y] == 0:
        MAP[x][y] = dice[dix][diy]
    tx, ty = dixy[(dix, diy)][5]
    if cmd == 1 or cmd == 2:
        turn(cmd)

        a = {d1: (1, 2), d2: (1, 0), d3: (3, 1), d4: (1, 1), 5: (2, 1)}
        b = {d1: (1, 1), d2: (3, 1), d3: (0, 1), d4: (2, 1), 5: (1, 2)}
        c = {d1: (1, 2), d2: (1, 0), d3: (0, 1), d4: (2, 1), 5: (3, 1)}
        d = {d1: (3, 1), d2: (1, 1), d3: (0, 1), d4: (2, 1), 5: (1, 0)}
        e = {d1: (1, 2), d2: (1, 0), d3: (1, 1), d4: (3, 1), 5: (0, 1)}
        f = {d1: (1, 2), d2: (1, 0), d3: (2, 1), d4: (0, 1), 5: (1, 1)}

        dixy = {
            (0, 1): a,
            (1, 0): b,
            (1, 1): c,
            (1, 2): d,
            (2, 1): e,
            (3, 1): f,
        }
    print(dice[tx][ty])
