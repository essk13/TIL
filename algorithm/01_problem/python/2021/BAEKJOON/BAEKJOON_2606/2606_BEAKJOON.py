def bfs(virus):
    queue = [virus]
    cnt = 0
    while queue:
        now = queue.pop(0)
        for i in range(1, N+1):
            if adj[now][i] == 1 and infected[i] == 0:
                infected[i] = 1
                queue.append(i)
                cnt += 1
    return cnt


N = int(input())
L = int(input())
adj = [[0] * (N+1) for _ in range(N+1)]
infected = [0] * (N+1)
infected[1] = 1

for i in range(L):
    st, ed = map(int, input().split())
    adj[st][ed] = 1
    adj[ed][st] = 1

ans = bfs(1)
print(ans)
