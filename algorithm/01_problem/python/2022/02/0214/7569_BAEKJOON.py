import sys
from collections import deque
input = sys.stdin.readline

dn = [-1, 0, 1, 0, 0, 0]
dm = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
M, N, H = map(int, input().split())
boxes = []
for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    boxes.append(box)

cnt = 0
tomato = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxes[h][n][m] == 1:
                visited[h][n][m] = 1
                tomato.append([h, n, m])
            elif boxes[h][n][m] == 0:
                cnt += 1

ans = 0
while True and cnt:
    nx = []
    while tomato:
        h, n, m = tomato.popleft()
        for i in range(6):
            nh, nn, nm = h + dh[i], n + dn[i], m + dm[i]
            if nh < 0 or nh >= H or nn < 0 or nn >= N or nm < 0 or nm >= M:
                continue
            if visited[nh][nn][nm]:
                continue
            if boxes[nh][nn][nm] != 0:
                continue

            cnt -= 1
            visited[nh][nn][nm] = 1
            nx.append([nh, nn, nm])

    ans += 1
    if cnt == 0:
        break
    elif not nx:
        ans = -1
        break
    tomato = deque(nx)

print(ans)
