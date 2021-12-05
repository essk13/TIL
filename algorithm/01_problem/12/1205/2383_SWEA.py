import sys
sys.stdin = open('input.txt', 'r')
'''
Fail
재 풀이 예정
'''

from collections import deque


def find(r, c):
    q = deque([(r, c, 0)])
    visited = [[0] * N for _ in range(N)]
    ret = []
    while q:
        y, x, m = q.popleft()
        if MAP[y][x] > 1:
            if ret:
                if ret[0][0] == m:
                    ret.append((m, MAP[y][x]))
            else:
                ret.append((m, MAP[y][x]))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
            if visited[ny][nx]: continue
            visited[ny][nx] = 1
            q.append((ny, nx, m + 1))
    ret.sort(key=lambda x:x[1])
    return ret[0]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    stairs = [[] for _ in range(11)]

    p = 1
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 1:
                m, stair = find(r, c)
                stairs[stair].extend([(m + 1, p)])
                p += 1

    stairs = list(map(sorted, stairs))
    p = [0] * 11

    ans = 0
    for s in range(1, 11):
        if stairs[s]:
            n = deque()
            for m, p in stairs[s]:
                if n and n[0] > m:
                    m = n[0]

                while n and n[0] + s < m:
                    n.popleft()

                if len(n) >= 3:
                    np = n.popleft()
                    m = np + s
                    while n and n[0] == np:
                        n.popleft()

                n.append(m)
                ans = max(ans, m + s)

    print('#{} {}'.format(tc+1, ans))