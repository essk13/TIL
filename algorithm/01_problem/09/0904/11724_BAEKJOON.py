from collections import deque


def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        now = queue.popleft()
        for i in range(1, N+1):
            if adj[now][i] == 1 and linked[i] == 0:
                linked[i] = 1
                queue.append(i)
    return 1


N, M = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]
linked = [0] * (N + 1)
for i in range(M):
    st, ed = map(int, input().split())
    adj[st][ed] = 1
    adj[ed][st] = 1

ans = 0
for j in range(1, N+1):
    if linked[j] == 0:
        linked[j] = 1
        ans += bfs(j)

print(ans)