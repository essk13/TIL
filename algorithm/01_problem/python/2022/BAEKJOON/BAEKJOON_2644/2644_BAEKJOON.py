import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

adj = [[0] * (n + 1) for _ in range(n + 1)]
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    adj[x][y] = 1
    adj[y][x] = 1

ans = -1
visited = [0] * (n + 1)
visited[a] = 1
q = deque([(a, 0)])
while q:
    now, count = q.popleft()
    if now == b:
        ans = count
        break

    for j in range(1, n + 1):
        if adj[now][j] and visited[j] == 0:
            visited[j] = 1
            q.append((j, count + 1))

print(ans)
