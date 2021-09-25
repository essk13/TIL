def dfs(now, lv):
    global max_lv, min_lv
    if now == 3:
        max_lv = max(lv, max_lv)
        min_lv = min(lv, min_lv)
        return
    for i in range(4):
        if adj[now][i] != 0 and visited[i] == 0:
            visited[i] = 1
            dfs(i, lv + adj[now][i])
            visited[i] = 0
    return


adj = [
    [0, 15, 10, 27],
    [2, 0, 0, 1],
    [0, 5, 0, 8],
    [0, 0, 0, 0],
]

visited = [0] * 4
visited[0] = 1

max_lv = 0
min_lv = 21e8

dfs(0, 0)
print(max_lv, min_lv)