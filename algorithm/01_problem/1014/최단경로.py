import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
st = int(input())
adj = [[] for _ in range(V+1)]
for i in range(E):
    n, nt, c = map(int, sys.stdin.readline().split())
    adj[n].append([c, nt])

min_heap = [(0, st)]
INF = 21e8
ret = [INF for _ in range(V+1)]
while min_heap:
    c, n = heapq.heappop(min_heap)
    if n == st:
        ret[n] = c

    for nc, np in adj[n]:
        if ret[np] > nc + c:
            ret[np] = nc + c
            heapq.heappush(min_heap, (c+nc, np))

for i in range(1, V+1):
    if ret[i] == INF:
        print('INF')
    else:
        print(ret[i])
