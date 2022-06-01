import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def count_air():
    global cheese
    ch = 0
    for r in range(R):
        for c in range(C):
            if MAP[r][c]:
                ch += 1
    cheese = ch

    visited[0][0] = 1
    nq = deque()
    sq = deque([[0, 0]])
    while sq:
        sr, sc = sq.popleft()
        for s in range(4):
            nsr, nsc = sr + dr[s], sc + dc[s]
            if nsr < 0 or nsr >= R or nsc < 0 or nsc >= C:
                continue
            if visited[nsr][nsc] or MAP[nsr][nsc]:
                continue
            visited[nsr][nsc] = 1
            sq.append([nsr, nsc])
            nq.append([nsr, nsc])
    return nq


def hole(hr, hc):
    hq = deque([[hr, hc]])
    pq = deque()
    while hq:
        pr, pc = hq.popleft()
        for p in range(4):
            npr, npc = pr + dr[p], pc + dc[p]
            if npr < 0 or npr >= R or npc < 0 or npc >= C:
                continue
            if visited[npr][npc] or MAP[npr][npc]:
                continue
            visited[npr][npc] = 1
            hq.append([npr, npc])
            pq.append([npr, npc])
    return pq


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
cheese = 0
q = count_air()
turn = len(q)

ans = -1
pre_c = 0
while q:
    i, j = q.popleft()
    turn -= 1
    if turn < 0:
        if cheese != 0:
            pre_c = cheese
        ans += 1
        turn = len(q) - 1

    for d in range(4):
        nr, nc = i + dr[d], j + dc[d]
        if nr < 1 or nr >= R-1 or nc < 1 or nc >= C-1:
            continue
        if visited[nr][nc]:
            continue

        visited[nr][nc] = 1
        q.append([nr, nc])
        if MAP[nr][nc] == 0:
            res = hole(nr, nc)
            q += res
            turn += len(res)
            continue
        cheese -= 1

print('{}\n{}'.format(ans, pre_c))
