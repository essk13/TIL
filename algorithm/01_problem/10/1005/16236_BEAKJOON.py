from collections import deque

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
bs = 2

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

qu = deque()
sy, sx = 0, 0
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            qu.append((i, j, 0))
            visited[i][j] = bs
            sy, sx = i, j
            break

sec = 0
eat = 0
tg = []
while qu:
    y, x, lv = qu.popleft()

    if 0 < MAP[y][x] < bs:
        tg.append((y, x))

        while qu:
            r, c, lv2 = qu.popleft()
            if lv2 > lv:
                break
            if 0 < MAP[r][c] < bs:
                tg.append((r, c))

        tg.sort(key=lambda x:(x[0], x[1]))
        y, x = tg[0][0], tg[0][1]
        eat += 1
        sec += lv
        MAP[y][x] = 9
        MAP[sy][sx] = 0
        sy, sx = y, x
        qu = deque([(y, x, 0)])
        visited = [[0] * N for _ in range(N)]
        tg = []

        if eat == bs:
            bs += 1
            eat = 0
        continue

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if MAP[ny][nx] <= bs and visited[ny][nx] == 0:
                visited[ny][nx] = bs
                qu.append((ny, nx, lv+1))

print(sec)
