# from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]

for tc in range(int(input())):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    # Q = deque()
    Q = [0] * (N*M)
    front = -1
    rear = -1

    for y in range(N):
        for x in range(M):
            if MAP[y][x] == 'W':
                # Q.append((y, x))
                rear += 1
                Q[rear] = (y, x)
                visited[y][x] = 0

    # while Q:
        # ny, nx = Q.popleft()
    while front != rear:
        front += 1
        ny, nx = Q[front]
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]

            if 0 <= ty < N and 0 <= tx < N:
                if MAP[ty][tx] == 'L' and visited[ty][tx] == -1:
                    visited[ty][tx] = visited[ny][nx] + 1
                    rear += 1
                    Q[rear] = (ty, tx)

    ans = 0

    for i in visited:
        for j in i:
            ans += j

    print('#{} {}'.format(tc+1, ans))
