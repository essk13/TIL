import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


def move():
    global MAP
    now = [st]
    while now:
        que = deque(now)
        next = []
        new_MAP = [['.' for _ in range(8)] for _ in range(8)]
        for w in range(len(walls)):
            y, x = walls[w]
            if y + 1 < 8:
                new_MAP[y+1][x] = '#'
                walls[w] = [y+1, x]

        for y, x in now:
            if new_MAP[y][x] != '#':
                next.append([y, x])

        while que:
            r, c = que.popleft()
            if (r, c) == (0, 7):
                return 1

            for i in range(8):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr >= 8 or nc < 0 or nc >= 8: continue
                if visited[nr][nc]: continue
                if MAP[nr][nc] == '#' or new_MAP[nr][nc] == '#': continue

                visited[nr][nc] = 1
                next.append([nr, nc])

        MAP = deque(new_MAP)
        now = next[:]
    return 0


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

MAP = [list(input().strip()) for _ in range(8)]
st = [7, 0]
walls = []
for r in range(8):
    for c in range(8):
        if MAP[r][c] == '#':
            walls.append([r, c])

if walls:
    visited = [[0] * 8 for _ in range(8)]
    visited[7][0] = 1

    ans = move()
    print(ans)
else:
    print(1)
