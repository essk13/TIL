N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
NOW = [[[] for _ in range(N)] for _ in range(N)]
player = [0] * (K + 1)
n_p = [[0, 0] for _ in range(K + 1)]
for i in range(1, K+1):
    y, x, p = map(int, input().split())
    NOW[y-1][x-1].append(i)
    n_p[i][0] = y - 1
    n_p[i][1] = x - 1
    player[i] = p

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

play = 1
end = False
while play <= 1000:
    for x in range(1, K+1):
        if len(n_p[x]) == 2:
            r, c = n_p[x][0], n_p[x][1]
            if len(NOW[r][c]) != 0:
                p = player[NOW[r][c][0]]
                tr, tc = r + dr[p], c + dc[p]
                if 0 <= tr < N and 0 <= tc < N:
                    if len(NOW[tr][tc]) != 0:
                        if MAP[tr][tr] == 2:
                            if player[NOW[r][c][0]] == 1 or player[NOW[r][c][0]] == 3:
                                player[NOW[r][c][0]] += 1
                            else:
                                player[NOW[r][c][0]] -= 1
                            p = player[NOW[r][c][0]]
                            tr, tc = r + dr[p], c + dc[p]
                            if MAP[tr][tc] == 2:
                                continue
                        if 0 <= tr < N and 0 <= tc < N:
                            NOW[tr][tc] = NOW[tr][tc] + NOW[r][c]
                            n_p[x] = []
                            if len(NOW[tr][tc]) >= 4:
                                end = True
                                break
                            NOW[r][c] = []
                            if MAP[tr][tc] == 1:
                                NOW[tr][tc].reverse()
                    else:
                        NOW[r][c], NOW[tr][tc] = NOW[tr][tc], NOW[r][c]
                else:
                    if player[NOW[r][c][0]] == 1 or player[NOW[r][c][0]] == 3:
                        player[NOW[r][c][0]] += 1
                    else:
                        player[NOW[r][c][0]] -= 1
                    p = player[NOW[r][c][0]]
                    tr, tc = r + dr[p], c + dc[p]
                    if MAP[tr][tc] == 2:
                        continue
                    NOW[tr][tc] = NOW[tr][tc] + NOW[r][c]
                    n_p[x] = []
                    if len(NOW[tr][tc]) >= 4:
                        end = True
                        break
                    NOW[r][c] = []
                    if MAP[tr][tc] == 1:
                        NOW[tr][tc].reverse()
    if end:
        break

    play += 1

if end:
    print(play)
else:
    print(-1)
