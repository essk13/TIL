def solution(n, start, end, roads, traps):
    def trap(now):
        for c in range(n + 1):
            adj[now][c], adj[c][now] = adj[c][now], adj[now][c]
        return

    def dfs(now, cnt):
        if cnt >= ans[0]:
            return

        if now == end:
            ans[0] = min(ans[0], cnt)
            return

        if now in traps:
            trap(now)

        for c in range(n + 1):
            if visited[c] > 1 or c == start: continue
            if adj[now][c]:
                visited[c] += 1
                dfs(c, cnt + adj[now][c])
                visited[c] -= 1

        if now in traps:
            trap(now)
        return

    adj = [[0] * (n + 1) for _ in range(n + 1)]
    for p, q, s in roads:
        if adj[p][q]:
            adj[p][q] = min(s, adj[p][q])
        else:
            adj[p][q] = s

    visited = [0] * (n + 1)
    ans = [21e8]
    dfs(start, 0)

    return ans[0]