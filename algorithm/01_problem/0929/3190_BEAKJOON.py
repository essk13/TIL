from collections import deque

N = int(input())
MAP = [[0]*N for _ in range(N)]
MAP[0][0] = 7
K = int(input())
for a in range(K):
    y, x = map(int, input().split())
    MAP[y-1][x-1] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

qu = deque([(0, 0)])
d = 0

t = 0
L = int(input())
cmd = [input().split() for _ in range(L)]

while qu:
    t += 1
    y, x = qu[0]
    ty, tx = y + dy[d], x + dx[d]
    if ty < 0 or tx < 0 or ty >= N or tx >= N: break
    if (ty, tx) in qu: break
    if cmd and t == int(cmd[0][0]):
        if cmd[0][1] == 'D':
            d += 1
            if d > 3: d = 0
        else:
            d -= 1
            if d < 0: d = 3
        del(cmd[0])
    if MAP[ty][tx] == 1:
        qu.appendleft((ty, tx))
        MAP[ty][tx] = 7
    else:
        qu.appendleft((ty, tx))
        MAP[ty][tx] = 7
        MAP[qu[-1][0]][qu[-1][1]] = 0
        qu.pop()

print(t)
