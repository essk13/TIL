import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def check_dust(r, c):
    q = deque([(r, c, 0)])
    visited = [[0] * w for _ in range(h)]
    visited[r][c] = 1
    while q:
        y, x, m = q.popleft()
        for i in range(4):
            nr, nc = y + dr[i], x + dc[i]
            if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
            if MAP[nr][nc] == 'x': continue
            if visited[nr][nc]: continue
            visited[nr][nc] = 1

            if MAP[nr][nc] in list(range(10)):
                adj[num][MAP[nr][nc]] = min(adj[num][MAP[nr][nc]], m + 1)
                adj[MAP[nr][nc]][num] = min(adj[MAP[nr][nc]][num], m + 1)
            q.append((nr, nc, m + 1))
    return


def shortest(now, move):
    global ans
    if min(done) > 0:
        ans = min(move, ans)
        return
    if move > ans:
        return

    for i in range(len(dust)):
        if done[i] == 0:
            done[i] = 1
            shortest(i, move + adj[now][i])
            done[i] = 0
    return


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break

    MAP = [list(input().strip()) for _ in range(h)]

    now = []
    dust = []
    num = 1
    # 청소기 위치 = 0, 먼지 위치 = 1 ~ 10 으로 초기화
    # 청소기와 먼지 위치 저장
    for r in range(h):
        for c in range(w):
            if MAP[r][c] == 'o':
                MAP[r][c] = 0
                now = [(r, c)]
            elif MAP[r][c] == '*':
                MAP[r][c] = num
                dust.append((r, c))
                num += 1

    dust = now + dust
    adj = [[21e8] * len(dust) for _ in range(len(dust))]
    # 청소기와 먼지간의 최소 이동거리 계산 (인접 리스트 방식)
    for num in range(len(dust)):
        dy, dx = dust[num]
        check_dust(dy, dx)

    # 청소기에서 시작하여 모든 먼지를 제거하는 경우의 최소값 계산
    done = [0] * len(dust)
    done[0] = 1
    ans = 21e8
    shortest(0, 0)

    if ans < 21e8:
        print(ans)
    else:
        print(-1)
