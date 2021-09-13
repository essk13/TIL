from collections import deque


def bfs(y, x, height):
    queue = deque()
    queue.append([y, x])
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < N:
                if MAP[ty][tx] > height and visited[ty][tx] != height:
                    visited[ty][tx] = height
                    queue.append([ty, tx])
    return 1


dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans = 1
for h in range(1, 100):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] > h and visited[r][c] != h:
                visited[r][c] = h
                cnt += bfs(r, c, h)

    ans = max(ans, cnt)

print(ans)
