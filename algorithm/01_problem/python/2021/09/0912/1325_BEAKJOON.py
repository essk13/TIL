from collections import deque


def bfs(pc):
    queue = deque()
    queue.append(pc)
    hacking = [0] * (N + 1)
    hacking[pc] = 1
    cnt = 0
    while queue:
        now = queue.popleft()
        for i in range(len(adj[now])):
            if hacking[adj[now][i]] == 0:
                hacking[adj[now][i]] = 1
                cnt += 1
                queue.append(adj[now][i])
    return cnt


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for i in range(M):
    t1, t2 = map(int, input().split())
    adj[t2].append(t1)

hack = [0] * (N+1)
ans = 0
for j in range(1, N+1):
    cnt = bfs(j)
    ans = max(ans, cnt)
    if ans == cnt:
        hack[j] = ans

for c in range(1, N+1):
    if hack[c] == max(hack):
        print(c, end=' ')
