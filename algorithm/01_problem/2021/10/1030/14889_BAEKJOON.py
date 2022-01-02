import sys
I = sys.stdin.readline


def dfs(player, lv):
    global ans
    if lv == N // 2:
        st, lk = 0, 0
        for i in range(N):
            for j in range(N):
                if u[i] and u[j]: st += adj[i][j]
                elif not u[i] and not u[j]: lk += adj[i][j]
        ans = min(ans, abs(st - lk))

    for i in range(player, N):
        if u[i]:
            u[i] = 0
            dfs(player + 1, lv + 1)
            u[i] = 1
    return


N = int(I())
adj = [list(map(int, I().split())) for _ in range(N)]
u = [1] * N

ans = 21e8
dfs(0, 0)
print(ans)
