def maze_run(y, x):
    global ans
    if maze[y][x] == 3:
        ans = 1
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 16 and 0 <= nx < 16:
            if maze[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                maze_run(ny, nx)
                visited[ny][nx] = 0
    return


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = 10
for tc in range(T):
    case = '#' + input()
    maze = [list(map(int, list(input()))) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    visited[1][1] = 1

    ans = maze_run(1, 1)
    print('#{} {}'.format(tc+1, ans))
