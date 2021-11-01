import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
candy = [list(input().rstrip()) for _ in range(N)]
u = [[1] * N for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

qu = deque()
for y in range(N):
    for x in range(N):
        if u [y][x]:
            for i in range(4):
                r, c = y + dy[i], x + dx[i]
                if r < 0 or r >= N or c < 0 or c >= N: continue
                if candy[y][x] == candy[r][c]: continue
                qu.append((y, x, r, c))
                u[y][x] = u[r][c] = 0

ans = 0
while qu:
    if ans == N: break
    n_candy = deepcopy(candy)
    y, x, r, c = qu.popleft()
    n_candy[y][x], n_candy[r][c] = n_candy[r][c], n_candy[y][x]

    ret1 = ret2 = 0
    for i in range(N):
        cnt1 = [1, 1]
        cnt2 = [1, 1]
        for j in range(1, N):
            if n_candy[i][j-1] == n_candy[i][j]:
                cnt1[0] += 1
            if n_candy[i][j-1] != n_candy[i][j] or j == N - 1:
                cnt1[1] = max(cnt1[0], cnt1[1])
                cnt1[0] = 1

            if n_candy[j-1][i] == n_candy[j][i]:
                cnt2[0] += 1
            if n_candy[j-1][i] != n_candy[j][i] or j == N - 1:
                cnt2[1] = max(cnt2[0], cnt2[1])
                cnt2[0] = 1

        ret1 = max(ret1, cnt1[1])
        ret2 = max(ret2, cnt2[1])

    ans = max(ret1, ret2, ans)

print(ans)
