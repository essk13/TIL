def bfs(y, x):
    queue = [[y, x]]
    while queue:
        now = queue.pop(0)
        now_y, now_x = now[0], now[1]
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if farm[ny][nx] == 1 and check[ny][nx] == 0:
                    check[ny][nx] = 1
                    queue.append([ny, nx])
    return 1


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]
    check = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    cnt = 0
    for r in range(N):
        for c in range(M):
            if farm[r][c] == 1 and check[r][c] == 0:
                cnt += bfs(r, c)

    print(cnt)
