def omok(n):
    global win
    if MAP[y][x] == n:
        for i in range(4):
            cnt = 1
            ny = y + dy[i]
            nx = x + dx[i]
            noy = y + no_y[i]
            nox = x + no_x[i]
            if 0 <= ny < 19 and 0 <= nx < 19:
                if 0 <= noy < 19 and 0 <= nox < 19:
                    while MAP[ny][nx] == n and MAP[noy][nox] != n:
                        cnt += 1
                        if 0 <= ny + dy[i] < 21 and 0 <= nx + dx[i] < 21:
                            ny += dy[i]
                            nx += dx[i]
                        else:
                            break
                        if cnt > 5:
                            cnt = 0
                            break
                    if cnt == 5:
                        win = n
                        first[0], first[1] = y, x

                        return


MAP = [[0] * 21]
MAP = MAP + [[0] + list(map(int, input().split()))  + [0] for _ in range(19)]
MAP = MAP + [[0] * 21]

dy = [0, 1, 1, -1]
dx = [1, 0, 1, 1]

no_y = [0, -1, -1, 1]
no_x = [-1, 0, -1, -1]

win = 0
first = [0, 0]
for y in range(21):
    for x in range(21):
        if MAP[y][x] != 0:
            omok(MAP[y][x])

        if win:
            break

    if win:
        break

if win:
    print(win)
    print(*first)
else:
    print(win)
