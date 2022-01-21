import sys, heapq
input = sys.stdin.readline
'''
Fail 재풀이 예정
'''

def dijkstra():
    visited = [21e8] * (n + 1)
    visited[s] = 0
    min_ = []
    for d, c in adj[s]:
        if visited[d] == 0: continue
        visited[d] = c

        if s == g or d == g:
            heapq.heappush(min_, (c, d, 1, 0))
        elif s == h or d == h:
            heapq.heappush(min_, (c, d, 0, 1))
        elif (s == g and d == h) or (s == h and d == g):
            heapq.heappush(min_, (c, d, 1, 1))
        else:
            heapq.heappush(min_, (c, d, 0, 0))

    can = [0] * (n + 1)
    while min_:
        dist, now, pg, ph = heapq.heappop(min_)
        if now in destination:
            if (pg, ph) == (1, 1):
                can[now] = 1
            else:
                can[now] = 0

        for d, c in adj[now]:
            nc = c + dist
            if visited[d] <= nc: continue
            visited[d] = nc

            if d == g:
                heapq.heappush(min_, (nc, d, 1, ph))
            elif d == h:
                heapq.heappush(min_, (nc, d, pg, 1))
            else:
                heapq.heappush(min_, (nc, d, pg, ph))

    res = []
    for d in destination:
        if visited[d] < 21e8 and can[d] == 1:
            res.append(d)

    res.sort()
    return res


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

    ans = dijkstra()
    print(' '.join(map(str, ans)))
