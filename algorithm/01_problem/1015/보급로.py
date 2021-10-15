import sys
sys.stdin = open('보급로.txt', 'r')

import heapq

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, list(input()))) for _ in range(N)]
    done = [[21e8] * N for _ in range(N)]

    min_heap = [(0, 0, 0)]
    ans = 0
    while min_heap:
        time, r, c = heapq.heappop(min_heap)
        if (r, c) == (N-1, N-1):
            ans = time
            break

        for i in range(4):
            y, x = r + dy[i], c + dx[i]
            if y < 0 or y >= N or x < 0 or x >= N: continue
            T = MAP[y][x] + time
            if done[y][x] > T:
                done[y][x] = T
                heapq.heappush(min_heap, (T, y, x))

    print('#{} {}'.format(tc+1, ans))
