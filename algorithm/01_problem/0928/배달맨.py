from collections import deque

def bfs(r, c, n):
    global time, now
    qu = deque([(r, c, 0, [(r, c)])])
    while qu:
        y, x, lv, vd = qu.popleft()
        if MAP[y][x] == str(n):
            time += lv
            now = [y, x]
            return
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < H and 0 <= nx < W:
                if MAP[ny][nx] != '#' and (ny, nx) not in vd:
                    qu.append((ny, nx, lv+1, vd + [(ny, nx)]))


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    H, W, N = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]

    time = 0
    now = [0, 0]
    for i in range(1, N+1):
        bfs(now[0], now[1], i)

    print('#{} {}'.format(tc+1, time))
