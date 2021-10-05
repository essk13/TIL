from collections import deque

dy = [0, 1]
dx = [1, 0]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    total = [[21e8] * N for _ in range(N)]
    total[0][0] = MAP[0][0]

    path = deque([[0, 0]])
    while path:
        y, x = path.popleft()
        if y == N - 1 and x == N - 1:
            break
        for i in range(2):
            ny, nx = y + dy[i], x + dx[i]
            if ny < N and nx < N:
                if total[ny][nx] > total[y][x] + MAP[ny][nx]:
                    total[ny][nx] = total[y][x] + MAP[ny][nx]
                    path.append([ny, nx])

    print('#{} {}'.format(tc+1, total[N-1][N-1]))
