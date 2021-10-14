import heapq

for tc in range(int(input())):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    visited = [21e8] * (N + 1)
    for i in range(E):
        st, ed, l = map(int, input().split())
        adj[st].append([l, ed])

    min_heap = [(0, 0)]
    ans = 21e8
    while min_heap:
        l, n = heapq.heappop(min_heap)
        if n == N:
            ans = min(ans, l)
            continue

        for le, nt in adj[n]:
            if visited[nt] > l + le:
                visited[nt] = l + le
                heapq.heappush(min_heap, (l+le, nt))
    print('#{} {}'.format(tc+1, ans))
