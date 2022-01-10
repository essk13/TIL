import heapq

adj = {
    'A' : [(3,'D'), (6,'C')],
    'B' : [(3,'A')],
    'C' : [(2,'D')],
    'D' : [(1,'C'), (1,'B')],
    'E' : [(4,'B'), (2,'D')],
}

ret = {
    'A': -1,
    'B': -1,
    'C': -1,
    'D': -1,
    'E': -1,
}

min_heap = [(0, 'A')]
while min_heap:
    nc, n = heapq.heappop(min_heap)
    if ret[n] != -1: continue

    for c, nt in adj[n]:
        heapq.heappush(min_heap, (nc+c, nt))

    ret[n] = nc

print(ret)
