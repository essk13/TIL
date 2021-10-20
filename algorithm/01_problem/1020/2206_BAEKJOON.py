from collections import deque

N, M = map(int, input().split())
MAP = [input() for _ in range(N)]
ck = [[1] * M for _ in range(N)]
bk = [[1] * M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

qu = deque([(1, 1, 0, 0)])
while qu:
    cnt, b, r, c = qu.popleft()
    if (r, c) == (N-1, M-1):
        print(cnt)
        break

    for i in range(4):
        y, x = r + dy[i], c + dx[i]
        if y < 0 or y >= N or x < 0 or x >= M: continue
        C = cnt + 1
        if b and MAP[y][x] == '1' and bk[y][x]:
            bk[y][x] = 0
            qu.append((C, 0, y, x))

        if MAP[y][x] == '0':
            if b and ck[y][x]:
                ck[y][x] = 0
                qu.append((C, b, y, x))
            if b == 0 and bk[y][x]:
                bk[y][x] = 0
                qu.append((C, b, y, x))

else:
    print(-1)
