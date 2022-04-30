import sys
from collections import deque
input = sys.stdin.readline


def bfs(st):
    global ans
    q = deque()
    used = [[0] * (V+1) for _ in range(V+1)]
    for nxt in range(1, V+1):
        if adj[st][nxt]:
            used[st][nxt] = 1
            q.append((nxt, adj[st][nxt]))

    while q:
        now, total = q.popleft()
        if now == st:
            ans = min(ans, total)

        if total >= ans:
            continue

        for nxt in range(1, V+1):
            if adj[now][nxt]:
                if used[now][nxt]:
                    continue
                used[now][nxt] = 1

                nt = total + adj[now][nxt]
                if nt >= ans:
                    continue
                q.append((nxt, total + adj[now][nxt]))
    return


V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a][b] = c

ans = 4000001
for i in range(1, V+1):
    bfs(i)

if ans == 4000001:
    print(-1)
else:
    print(ans)
