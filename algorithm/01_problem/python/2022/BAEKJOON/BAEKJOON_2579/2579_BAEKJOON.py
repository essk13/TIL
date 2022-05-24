import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stair = [0] * (n + 1)
for i in range(1, n + 1):
    stair[i] = int(input())

ans = 0
visited = [0] * (n + 1)
q = deque([(0, 0, 0)])
while q:
    now, cont, score = q.popleft()
    if now == n:
        ans = max(ans, score)
        continue

    for j in range(1, 3):
        nxt = now + j
        if nxt > n:
            continue

        ns = score + stair[nxt]
        if ns <= visited[nxt]:
            continue

        if j == 1:
            if cont >= 2:
                continue
            q.append((nxt, cont + 1, ns))
        else:
            q.append((nxt, 1, ns))

print(ans)
