from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]
    visited = [[1] * M for _ in range(N)]

    qu = deque()
    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 'W':
                qu.append((y, x, 0))

    ans = 0
    while qu:
        r, c, lv = qu.popleft()
        ans += lv
        for i in range(4):
            ny, nx = r + dy[i], c + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if MAP[ny][nx] == 'L' and visited[ny][nx]:
                    visited[ny][nx] = 0
                    qu.append((ny, nx, lv+1))

    print('#{} {}'.format(tc+1, ans))
