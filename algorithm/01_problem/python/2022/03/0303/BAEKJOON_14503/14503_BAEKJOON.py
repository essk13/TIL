import sys
input = sys.stdin.readline
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def clean(r, c):
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    cnt = 1
    while True:
        nd = robot[2]
        for d in range(4):
            nd = (nd + 3) % 4
            nr, nc = robot[0] + dr[nd], robot[1] + dc[nd]
            if visited[nr][nc] or MAP[nr][nc]: continue

            visited[nr][nc] = 1
            robot[0], robot[1], robot[2] = nr, nc, nd
            cnt += 1
            break
        else:
            nd = (nd + 2) % 4
            nr, nc = robot[0] + dr[nd], robot[1] + dc[nd]
            if MAP[nr][nc]: break

            robot[0], robot[1] = nr, nc
    stop = 1
    stop += 1
    return cnt


N, M = map(int, input().split())
robot = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(N)]

ans = clean(robot[0], robot[1])
print(ans)
