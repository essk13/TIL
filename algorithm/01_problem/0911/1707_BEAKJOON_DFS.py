def dfs(node, lv):
    ret = True
    for x in range(len(adj[node])):
        if lv == 1:
            if visited[adj[node][x]] == 0:
                visited[adj[node][x]] = 2
                ret = dfs(adj[node][x], 2)
                if not ret:
                    return ret
            elif visited[adj[node][x]] == lv:
                return False
        elif lv == 2:
            if visited[adj[node][x]] == 0:
                visited[adj[node][x]] = 1
                ret = dfs(adj[node][x], 1)
                if not ret:
                    return ret
            elif visited[adj[node][x]] == lv:
                return False

    return ret


K = int(input())
for tc in range(K):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        st, ed = map(int, input().split())
        adj[st].append(ed)
        adj[ed].append(st)

    for x in range(1, V+1):
        if visited[x] == 0:
            visited[x] = 1
            ret = dfs(x, 1)
            if not ret:
                 break

    if ret:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)
