def start():
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                return [y, x]


def maze_run():
    while queue:
        now = queue.pop(0)
        y = now[0]
        x = now[1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
                    if maze[ny][nx] == 3:
                        return visited[ny][nx] - 2
    return 0


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    queue = []
    st = start()
    queue.append(st)
    visited[st[0]][st[1]] = 1
    ans = maze_run()

    print('#{} {}'.format(tc+1, ans))
