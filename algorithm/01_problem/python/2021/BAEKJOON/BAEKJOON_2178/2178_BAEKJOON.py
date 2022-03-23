from collections import deque

N, M = map(int, input().split())
MAP = [input() for _ in range(N)]
visited = [[1] * M for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
qu = deque([(1, 0, 0)])
while qu:
    cnt, r, c = qu.popleft()
    if (r, c) == (N-1, M-1):
        print(cnt)
        break
    for i in range(4):
        y, x = r + dy[i], c + dx[i]
        if y < 0 or y >= N or x < 0 or x >= M: continue
        if MAP[y][x] == '1' and visited[y][x]:
            visited[y][x] = 0
            qu.append((cnt+1, y, x))
