import sys
from collections import deque
'''
18% 틀렸습니다.(Fail)
재풀이 예정
'''
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def check(y, x):
    que = deque([(y, x)])
    cluster = [(y, x)]
    outline = [(y, x)]
    while que:
        r, c = que.popleft()
        if r == R - 1:
            return False
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if visited[nr][nc]: continue
            if cave[nr][nc] == '.': continue

            visited[nr][nc] = 1
            que.append((nr, nc))
            cluster.append((nr, nc))
            for i in range(4):
                nnr, nnc = nr + dr[i], nc + dc[i]
                if nnr < 0 or nnr >= R or nnc < 0 or nnc >= C: continue
                if cave[nnr][nnc] == '.':
                    outline.append((nr, nc))
                    break

    gravity(cluster, outline)
    return True


def gravity(cluster, outline):
    for r, c in cluster:
        cave[r][c] = '.'

    stop = False
    res = 1
    while True:
        for r, c in outline:
            if r + res >= R or cave[r + res][c] == 'x':
                stop = True
                res -= 1
                break
        else:
            res += 1
        if stop: break

    for r, c in cluster:
        cave[r + res][c] = 'x'
    return


R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
H = list(map(int, input().split()))

for turn in range(1, N + 1):

    if turn % 2:
        d = 0
        di = 'left'
    else:
        d = C - 1
        di = 'right'

    h = R - H[turn - 1]
    while 1:
        if cave[h][d] == 'x':
            cave[h][d] = '.'
            break

        if di == 'left':
            if d == C - 1:
                break
            d += 1
        else:
            if d == 0:
                break
            d -= 1

    visited = [[0] * C for _ in range(R)]
    for i in range(4):
        nr, nc = h + dr[i], d + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
        if visited[nr][nc]: continue
        if cave[nr][nc] == '.': continue

        visited[nr][nc] = 1
        res = check(nr, nc)
        if res:
            break

for i in range(R):
    print(''.join(cave[i]))
