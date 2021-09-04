def normal_p(y, x, color):
    queue = [[y, x]]
    while queue:
        now = queue.pop(0)
        now_y, now_x = now[0], now[1]
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if plate[ny][nx] == color and normal[ny][nx] == 0:
                    normal[ny][nx] = 1
                    queue.append([ny, nx])
    return 1


def blind_p(y, x, color):
    queue = [[y, x]]
    while queue:
        now = queue.pop(0)
        now_y, now_x = now[0], now[1]
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if (plate[ny][nx] == color[0] or plate[ny][nx] == color[-1]) and blind[ny][nx] == 0:
                    blind[ny][nx] = 1
                    queue.append([ny, nx])
    return 1


N = int(input())
plate = [input() for _ in range(N)]
blind = [[0] * N for _ in range(N)]
normal = [[0] * N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ans = [0, 0]
for r in range(N):
    for c in range(N):
        if normal[r][c] == 0:
            ans[0] += normal_p(r, c, plate[r][c])
        if blind[r][c] == 0:
            if plate[r][c] == 'B':
                ans[1] += blind_p(r, c, ['B'])
            else:
                ans[1] += blind_p(r, c, ['R', 'G'])

print(*ans)
