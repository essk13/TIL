import sys
import heapq

N = int(sys.stdin.readline())
bus = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
for i in range(bus):
    s, e, c = map(int, sys.stdin.readline().split())
    adj[s].append([c, e])
st, ed = map(int, sys.stdin.readline().split())

min_heap = [(0, st)]
visited = [21e8] * (N+1)
visited[st] = 0

ans = 21e8
while min_heap:
    cost, now = heapq.heappop(min_heap)
    if now == ed:
        ans = min(ans, cost)
        continue
    if cost >= ans: continue

    for c, s in adj[now]:
        if visited[s] > cost + c:
            visited[s] = cost + c
            heapq.heappush(min_heap, (cost + c, s))

print(ans)
