from collections import deque


def bfs(y, x):
    queue = deque()
    queue.append([y, x])
    while queue:
        ny, nx = queue.popleft()
        for i in range(8):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < r and 0 <= tx < c:
                if MAP[ty][tx] == 1 and visited[ty][tx] == 0:
                    visited[ty][tx] = 1
                    queue.append([ty, tx])
    return 1


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

map_ = deque()
map_.append(list(map(int, input().split())))
while map_:
    c, r = map_.popleft()
    if r == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(r)]
    visited = [[0] * c for _ in range(r)]

    cnt = 0
    for y in range(r):
        for x in range(c):
            if MAP[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = 1
                cnt += bfs(y, x)

    print(cnt)
    map_.append(list(map(int, input().split())))
