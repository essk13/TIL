import heapq

M, N = map(int, input().split())
MAP = [input() for _ in range(N)]
bk = [[1] * M for _ in range(N)]
bk[0][0] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

min_ = [(0, 0, 0)]
while min_:
    b, r, c = heapq.heappop(min_)
    if (r, c) == (N-1, M-1):
        print(b)
        break
    for i in range(4):
        y, x = r + dy[i], c + dx[i]
        if y < 0 or y >= N or x < 0 or x >= M: continue
        if MAP[y][x] == '0' and bk[y][x]:
            bk[y][x] = 0
            heapq.heappush(min_, (b, y, x))
            continue
        if bk[y][x]:
            bk[y][x] = 0
            heapq.heappush(min_, (b+1, y, x))

