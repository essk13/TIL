import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    st, ed, cost = map(int, input().split())
    adj[st].append([ed, cost])
a, b = map(int, input().split())

visited = [21e8] * (n + 1)
route = [[] for _ in range(n + 1)]
heap = []
heapq.heappush(heap, [0, a])
while heap:
    cost, now = heapq.heappop(heap)
    if cost >= visited[b]: continue
    if now == a:
        route[a].append(a)
        visited[a] = 0

    for de, c in adj[now]:
        nc = cost + c
        if nc >= visited[de]: continue
        visited[de] = nc
        heapq.heappush(heap, [nc, de])
        route[de] = route[now][:] + [de]

print(visited[b])
print(len(route[b]))
print(' '.join(map(str, route[b])))
