def dfs(cnt, total, x):
    global ans, now
    if cnt == K:
        ans = max(ans, total)
        return

    for r in range(x, N):
        for c in range(M):
            if [r, c] in now:
                continue
            if not now:
                now.append([r, c])
                dfs(cnt + 1, MAP[r][c], r)
                now.pop()
            else:
                stop = False
                for i, j in now:
                    for d in range(4):
                        ni, nj = i + dr[d], j + dc[d]
                        if (r, c) == (ni, nj):
                            stop = True
                            break
                    if stop: break
                else:
                    now.append([r, c])
                    dfs(cnt + 1, total + MAP[r][c], r)
                    now.pop()
    return


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = -21e8
now = []
dfs(0, 0, 0)
print(ans)
