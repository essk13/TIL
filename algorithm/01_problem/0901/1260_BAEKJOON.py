def dfs(now):
    print(now, end=' ')
    for i in range(1, N+1):
        if adj[now][i] == 1 and visited1[i] == 0:
            visited1[i] = 1
            dfs(i)
    return


def bfs(now):
    queue = [now]
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for i in range(1, N+1):
            if adj[node][i] == 1 and visited2[i] == 0:
                visited2[i] = 1
                queue.append(i)


N, M, V = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)
visited1[V] = 1
visited2[V] = 1

for path in range(M):
    st, ed = map(int, input().split())
    adj[st][ed] = 1
    adj[ed][st] = 1

dfs(V)
print()
bfs(V)

