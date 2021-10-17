import heapq

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    min_ = [(MAP[0][0], 0, 0)]
    u = [[21e8] * N for _ in range(N)]
    u[0][0] = MAP[0][0]
    while min_:
        t, r, c = heapq.heappop(min_)
        if (r, c) == (N-1, N-1):
            break
        for i in range(4):
            y, x = r + dy[i], c + dx[i]
            if y < 0 or y >= N or x < 0 or x >= N: continue
            T = t + MAP[y][x]
            if u[y][x] > T:
                u[y][x] = T
                heapq.heappush(min_, (T, y, x))
    print('#{} {}'.format(tc+1, u[N-1][N-1]))
