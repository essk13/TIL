from collections import deque

N = int(input())
MAP = [[0]*N for _ in range(N)]
K = int(input())
for a in range(K):
    y, x = map(int, input().split())
    MAP[y-1][x-1] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

qu = deque([(0, 0)])
d = 0
move = [[0] * N for _ in range(N)]
move[0][0] = 7

t = 0
L = int(input())
g = False
for c in range(L):
    s, cmd = input().split()
    gt = int(s) - t
    for i in range(1, gt+1):
        t += 1
        y, x = qu[0]
        ny, nx = y + dy[d], x + dx[d]
        if ny < 0 or ny >= N or nx < 0 or nx >= N: g = True; break
        if (ny, nx) in qu: g = True; break
        if t == int(s):
            if cmd == 'D':
                d += 1
                if d > 3: d = 0
            else:
                d -= 1
                if d < 0: d = 3
        if MAP[ny][nx]: qu.appendleft((ny, nx)); move[ny][nx] = 7
        else:
            qu.appendleft((ny, nx)); move[ny][nx] = 7
            move[qu[-1][0]][qu[-1][1]] = 0; qu.pop()

    if g:
        break
if g:print(t)
else:
    while not g:
        t += 1
        y, x = qu[0]
        ny, nx = y + dy[d], x + dx[d]
        if ny < 0 or ny >= N or nx < 0 or nx >= N: g = True; break
        if (ny, nx) in qu: g = True; break
        if MAP[ny][nx]: qu.appendleft((ny, nx)); move[ny][nx] = 7
        else:
            qu.appendleft((ny, nx)); move[ny][nx] = 7
            move[qu[-1][0]][qu[-1][1]] = 0; qu.pop()

    print(t)