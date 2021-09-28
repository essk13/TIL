from collections import deque

def gravity(r, c):
    qu = deque([(r, c)])
    m = [(r, c)]
    nb = [(r, c)]
    while qu:
        ny, nx = qu.popleft()
        if r == h - 1 and ny == h:
            return
        elif ny == h + 1 or ny == -1:
            return
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 < -ty < R and 0 <= tx < C:
                if cave[ty][tx] != '.' and (ty, tx) not in m:
                    qu.append((ty, tx))
                    m.append((ty, tx))
                    if cave[ty + 1][tx] == '.':
                        nb.append((ty, tx))

    go = False
    for hi in range(1, abs(h)):
        for x in nb:
            if cave[x[0]+hi][x[1]] == '.' or (x[0]+hi, x[1]) in m:
                continue
            go = True
            break
        if go:
            nh = hi - 1
            break
    else:
        nh = abs(h) - 1

    m.sort(key=lambda x: -x[0])
    for nm in m:
        cave[nm[0]][nm[1]], cave[nm[0]+nh][nm[1]] = cave[nm[0]+nh][nm[1]], cave[nm[0]][nm[1]]
    return


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dr = [-1, 0, 0]
dc = [0, 1, -1]

R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]
N = int(input())
hi = list(map(int, input().split()))
for i in range(N):
    h = -hi[i]
    br, bc = 0, 0
    if i % 2:
        for j in range(C-1, -1, -1):
            if cave[h][j] == 'x':
                cave[h][j] = '.'
                br = h
                bc = j
                break
    else:
        for j in range(C):
            if cave[h][j] == 'x':
                cave[h][j] = '.'
                br = h
                bc = j
                break

    for j in range(3):
        nr, nc = br + dr[j], bc + dc[j]
        if 0 <= -nr < R and 0 <= nc < C:
            if cave[nr][nc] == 'x':
                gravity(nr, nc)
                break

for l in range(R):
    print(*cave[l])