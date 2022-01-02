from collections import deque

def bfs(y, x, path1, path2):
    global ret
    path = deque([[y, x, 0]])
    visited = [[0] * M for _ in range(N)]
    while path:
        py, px, lv = path.popleft()
        visited[py][px] = 1
        if lv + 1 >= ret:
            return 21e8
        for i in [path1, path2]:
            ny, nx = py + dy[i], px + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if MAP[ny][nx] == 'W':
                    return lv + 1
                elif visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    path.append([ny, nx, lv+1])

    return 21e8


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(M):
            ret = 21e8
            if MAP[r][c] == 'L':
                ret = min(bfs(r, c, 0, 1), ret)
                ret = min(bfs(r, c, 0, 3), ret)
                ret = min(bfs(r, c, 2, 1), ret)
                ret = min(bfs(r, c, 2, 3), ret)
                ans += ret

    print('#{} {}'.format(tc+1, ans))
