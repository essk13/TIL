N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
NOW = [[[] for _ in range(N)] for _ in range(N)]
cmd = [0] * (K + 1)
player = [[0, 0] for _ in range(K + 1)]
for i in range(1, K+1):
    y, x, p = map(int, input().split())
    NOW[y-1][x-1].append(i)
    player[i][0] = y - 1
    player[i][1] = x - 1
    cmd[i] = p

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

play = 1
end = False
while play <= 1000:
    for j in range(1, K+1):
        if len(player[j]) == 2:
            y, x = player[j]
            c = cmd[j]
            ty, tx = y + dy[c], x + dx[c]
            if 0 <= ty < N and 0 <= tx < N:
                if MAP[ty][tx] == 2:
                    if cmd[j] == 1 or cmd[j] == 3:
                        cmd[j] += 1
                    elif cmd[j] == 2 or cmd[j] == 4:
                        cmd[j] -= 1
                    c = cmd[j]
                    ty, tx = y + dy[c], x + dx[c]
                    if MAP[ty][tx] == 2:
                        continue
                if MAP[ty][tx] == 1:
                    if len(MAP[ty][tx]) != 0:
                        player[j] = []
                    NOW[ty][tx] = NOW[ty][tx] + NOW[y][x]
                    NOW[ty][tx].reverse()
                    NOW[y][x] = []
                else:
                    if len(MAP[ty][tx]) != 0:
                        player[j] = []
                    NOW[ty][tx] = NOW[ty][tx] + NOW[y][x]
                    NOW[y][x] = []
                if len(NOW[ty][tx]) >= 4:
                    end = True
                    break
            else:
                if cmd[j] == 1 or cmd[j] == 3:
                    cmd[j] += 1
                elif cmd[j] == 2 or cmd[j] == 4:
                    cmd[j] -= 1
                c = cmd[j]
                ty, tx = y + dy[c], x + dx[c]
                if MAP[ty][tx] == 2:
                    continue
                if MAP[ty][tx] == 1:
                    if len(MAP[ty][tx]) != 0:
                        player[j] = []
                    NOW[ty][tx] = NOW[ty][tx] + NOW[y][x]
                    NOW[ty][tx].reverse()
                    NOW[y][x] = []
                else:
                    if len(MAP[ty][tx]) != 0:
                        player[j] = []
                    NOW[ty][tx] = NOW[ty][tx] + NOW[y][x]
                    NOW[y][x] = []
                if len(NOW[ty][tx]) >= 4:
                    end = True
                    break
    if end:
        break

if end:
    print(play)
else:
    print(-1)