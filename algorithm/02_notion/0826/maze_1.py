def maze_run():
    while queue:
        now = queue.pop(0)
        y = now[0]
        x = now[1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 16 and 0 <= nx < 16:
                if maze[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                    if maze[ny][nx] == 3:
                        return 1
    return 0


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = 10
for tc in range(T):
    case = '#' + input()
    maze = [list(map(int,list(input()))) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    queue = []
    queue.append((1, 1))
    visited[1][1] = 1

    ans = maze_run()
    print('#{} {}'.format(tc+1, ans))
