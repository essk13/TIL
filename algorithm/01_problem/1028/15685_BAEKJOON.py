import sys
I = sys.stdin.readline

#     →, ↑, ←, ↓ // 방향배열
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def first_dragon(r, c):
    MAP[r][c] = 1
    y = r + dy[d]
    x = c + dx[d]
    MAP[y][x] = 1
    return (y, x)


def dragon(r, c, d):
    global directions
    directions.append(d)

    MAP[r][c] = 1
    y, x = r + dy[d], c + dx[d]
    MAP[y][x] = 1
    return (y, x)


def curve(cnt):
    next_d = [0] * cnt
    for d in range(cnt-1, -1, -1):
        next_d[d] = (directions[d] + 1) % 4
    return next_d


def count():
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    cnt = 0
    for y in range(101):
        for x in range(101):
            if MAP[y][x]:
                ck = 0
                ny, nx = y, x
                for i in range(4):
                    ny += dy[i]
                    nx += dx[i]
                    if ny < 0 or ny >= 101 or nx < 0 or nx >= 101: break
                    ck += MAP[ny][nx]

                if ck == 4: cnt += 1
    return cnt


N = int(I())
curves = [list(map(int, I().split())) for _ in range(N)]
MAP = [[0] * 101 for _ in range(101)]

for i in range(N):
    x, y, d, g = curves[i]
    y, x = first_dragon(y, x)
    directions = [d]
    next_d = [d]

    while g > 0:
        next_d = curve(len(directions))
        for d in next_d:
            y, x = dragon(y, x, d)
        g -= 1

ans = count()
print(ans)
