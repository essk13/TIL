import sys, heapq
input = sys.stdin.readline


def dijkstra(st):
    visited = [21e8] * (n + 1)
    visited[st] = 0
    heap = []
    for d, c in adj[st]:
        visited[d] = c
        heapq.heappush(heap, (c, d))
    while heap:
        dist, now = heapq.heappop(heap)
        for d, c in adj[now]:
            nc = dist + c
            if visited[d] <= nc: continue

            visited[d] = nc
            heapq.heappush(heap, (nc, d))
    return visited


for tc in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        adj[a].append([b, d])
        adj[b].append([a, d])

    destination = []
    for _ in range(t):
        destination.append(int(input().strip()))

    ans = []
    # s에서 출발한 모든 지점의 최단거리
    S = dijkstra(s)
    # g에서 출발한 모든 지점의 최단거리
    G = dijkstra(g)
    # h에서 출발한 모든 지점의 최단거리
    H = dijkstra(h)

    for de in destination:
        '''
        1) s에서 목적지 de까지의 최단거리
        2) s에서 경유지 g까지의 최단거리 + g에서 h 거리 + 경유지 h에서 목적지 de까지의 최단거리
        3) s에서 경유지 h까지의 최단거리 + h에서 g 거리 + 경유지 g에서 목적지 de까지의 최단거리
        
        1번이 2번 또는 3번과 같다면 이동 가능한 목적지
        '''
        if S[de] in (G[s] + G[h] + H[de], H[s] + H[g] + G[de]):
            ans.append(de)

    ans.sort()
    print(' '.join(map(str, ans)))
