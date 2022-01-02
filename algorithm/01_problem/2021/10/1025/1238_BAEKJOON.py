import sys, heapq
I = sys.stdin.readline


def dijkstra(t, x, to, adj):
    min_ = [(t, x)]
    to[x] = 0
    while min_:
        time, now = heapq.heappop(min_)

        for t, next in adj[now]:
            T = time + t
            if to[next] > T:
                to[next] = T
                heapq.heappush(min_,(T, next))
    return


N, M, X = map(int, I().split())
adj1 = [[] for _ in range(N+1)]
adj2 = [[] for _ in range(N+1)]
for i in range(M):
    st, ed, time = map(int, I().split())
    adj1[st].append([time, ed])
    adj2[ed].append([time, st])

to_X = [21e8] * (N + 1)
dijkstra(0, X, to_X, adj1)
to_H = [21e8] * (N + 1)
dijkstra(0, X, to_H, adj2)

ans = 0
for i in range(1, N+1):
    ans = max(ans, to_X[i] + to_H[i])

print(ans)
