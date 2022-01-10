import sys
sys.stdin = open('input_01.txt', 'r')

import heapq


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for tc in range(int(input())):
    M, N, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(M)]
    ck = [[21e8] * N for _ in range(M)]

    min_ = []
    heapq.heappush(min_, (0, L, M - 1, 0))
    ans = -1
    while min_:
        cnt, l, r, c = heapq.heappop(min_)
        if MAP[r][c] == 3:
            ans = cnt
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            n_cnt, nl = cnt, l
            if nr < 0 or nr >= M or nc < 0 or nc >= N: continue
            if ck[nr][nc] < n_cnt: continue

            if MAP[nr][nc] == 1:
                dl = L
                d_cnt = cnt + 1
                heapq.heappush(min_, (d_cnt, dl, nr, nc))

            nl -= 1
            ck[nr][nc] = n_cnt
            if nl or MAP[nr][nc] == 3:
                heapq.heappush(min_, (n_cnt, nl, nr, nc))

    print(ans)
