import sys, heapq
from copy import deepcopy
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

'''
FAIL
'''

def escape1(r, c):
    root = []
    heapq.heappush(root, (0, r, c, []))
    visited = [[0] * w for _ in range(h)]
    cnt = 21e8
    while root:
        door_cnt, y, x, door_position = heapq.heappop(root)
        if y in (0, h - 1) or x in (0, w - 1):
            res = door_cnt + escape2(door_position, prisoner[1])
            cnt = min(cnt, res)

        for i in range(4):
            nr, nc = y + dr[i], x + dc[i]
            if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
            if visited[nr][nc]: continue
            if MAP[nr][nc] == '*': continue

            visited[nr][nc] = 1
            if MAP[nr][nc] == '#':
                heapq.heappush(root, (door_cnt + 1, nr, nc, door_position + [(nr, nc)]))
            else:
                heapq.heappush(root, (door_cnt, nr, nc, door_position))
    return cnt


def escape2(position, prisoner_position):
    new_map = deepcopy(MAP)
    for y, x in position:
        new_map[y][x] = '.'

    r, c = prisoner_position
    min_ = []
    heapq.heappush(min_, (0, r, c))
    visited = [[0] * w for _ in range(h)]
    while min_:
        door_cnt, y, x = heapq.heappop(min_)
        if y in (0, h - 1) or x in (0, w - 1):
            return door_cnt

        for i in range(4):
            nr, nc = y + dr[i], x + dc[i]
            if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
            if visited[nr][nc]: continue
            if new_map[nr][nc] == '*': continue

            visited[nr][nc] = 1
            if new_map[nr][nc] == '#':
                heapq.heappush(min_, (door_cnt + 1, nr, nc))
            else:
                heapq.heappush(min_, (door_cnt, nr, nc))
    return 0


for tc in range(int(input())):
    h, w = map(int, input().split())
    MAP = [list(input().strip()) for _ in range(h)]

    ans = 0
    prisoner = []
    for r in range(h):
        for c in range(w):
            if MAP[r][c] == '$':
                prisoner.append((r, c))
            if len(prisoner) == 2:
                break

    r, c = prisoner[0]
    ans = escape1(r, c)
    print(ans)
