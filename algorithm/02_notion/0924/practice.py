from collections import deque

def bfs1(r, c):
    Q = deque([(r, c)])
    size = 0
    point = []
    while Q:
        y, x = Q.popleft()
        point.append((y, x, 0))
        size += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 8 and 0 <= nx < 9:
                if MAP[ny][nx] == '#' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    Q.append((ny, nx))
    return size, point


MAP = [
    '______###',
    '______###',
    '______###',
    '_____####',
    '____##___',
    '#________',
    '##_______',
    '###______',
]

visited = [[0] * 9 for _ in range(8)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ret = []
for y in range(8):
    for x in range(9):
        if MAP[y][x] == '#' and visited[y][x] == 0:
            visited[y][x] = 1
            ret.append(bfs1(y, x))

Q = deque()

if ret[0][0] > ret[1][0]:
    for i in range(len(ret[1][1])):
        Q.append(ret[1][1][i])
else:
    for i in range(len(ret[0][1])):
        Q.append(ret[0][1][i])

while Q:
    r, c, lv = Q.popleft()
    for j in range(4):
        ny, nx = r + dy[j], c + dx[j]
        if 0 <= ny < 8 and 0 <= nx < 9:
            if visited[ny][nx] != 1:
                pass