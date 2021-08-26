def dfs(start):
    print(start, end=' ')
    visited[start] = 1
    for i in range(1, N+1):
        if i in adj[start] and visited[i] == 0:
            visited[i] = 1
            dfs(i)
    return


def bfs(start):
    visited2 = [0] * (N + 1)
    queue = [start]
    visited2[start] = 1
    while queue:
        now = queue.pop(0)
        print(now, end=' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and i in adj[now]:
                visited2[i] = 1
                queue.append(i)
    return


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
for path in range(M):
    st, ed = map(int, input().split())
    adj[st].append(ed)
    adj[ed].append(st)

dfs(V)
print()
bfs(V)
