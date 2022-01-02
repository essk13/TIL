import heapq

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

tc = 1
while True:
    N = int(input())
    if N == 0: break
    cave = [list(map(int, input().split())) for _ in range(N)]
    min_heap = [(cave[0][0], 0, 0)]
    visited = [[21e8] * N for _ in range(N)]
    visited[0][0] = cave[0][0]
    ans = 0
    while min_heap:
        miss, r, c = heapq.heappop(min_heap)
        if (r, c) == (N-1, N-1):
            ans = miss
            break
        for i in range(4):
            y, x = r + dy[i], c + dx[i]
            if y < 0 or y >= N or x < 0 or x >= N: continue
            M = miss + cave[y][x]
            if visited[y][x] > M:
                visited[y][x] = M
                heapq.heappush(min_heap, (M, y, x))
    print('Problem {}: {}'.format(tc, ans))
    tc += 1

