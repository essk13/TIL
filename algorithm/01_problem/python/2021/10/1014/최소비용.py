import heapq

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[21e8] * N for _ in range(N)]
    min_heap = [(0, 0, 0)]
    ans = 21e8
    while min_heap:
        n = heapq.heappop(min_heap)
        if n[1] == N - 1 and n[2] == N - 1:
            ans = min(ans, n[0])
        for i in range(4):
            y, x = n[1] + dy[i], n[2] + dx[i]
            if y < 0 or y >= N or x < 0 or x >= N: continue

            if MAP[y][x] > MAP[n[1]][n[2]]:
                oil = n[0] + (MAP[y][x] - MAP[n[1]][n[2]]) + 1
            else:
                oil = n[0] + 1

            if oil < visited[y][x]:
                visited[y][x] = oil
                heapq.heappush(min_heap, (oil, y, x))
    print('#{} {}'.format(tc+1, ans))

# 1
# 3
# 0 2 1
# 0 1 1
# 1 1 1