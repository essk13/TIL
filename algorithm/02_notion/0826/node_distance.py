from collections import deque


def bfs(start):
    queue.append(start)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for node in range(1, V + 1):
            if adj[now][node] == 1 and visited[node] == 0:
                visited[node] = visited[now] + 1
                if node == ed:
                    return visited[ed] - 1
                queue.append(node)
    return 0


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    queue = deque()
    visited = [0] * (V + 1)

    for i in range(E):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1

    st, ed = map(int, input().split())
    ans = bfs(st)

    print('#{} {}'.format(tc+1, ans))
