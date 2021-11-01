def dfs(now, lv, total):
    global ans
    if lv == N - 1:
        total += adj[now][0]
        ans = min(ans, total)
        return
    for i in range(1, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, lv+1, total + adj[now][i])
            visited[i] = 0
    return


for tc in range(int(input())):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 21e8
    dfs(0, 0, 0)
    print('#{} {}'.format(tc+1, ans))
