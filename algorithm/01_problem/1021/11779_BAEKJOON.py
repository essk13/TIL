import sys, heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
for i in range(M):
    st, ed, cost = map(int, sys.stdin.readline().split())
    adj[st].append([cost, ed])
A, B = map(int, sys.stdin.readline().split())
vi = [21e8] * (N + 1)
vi[A] = 0

min_ = [(0, [A], A)]
while min_:
    cost, visited, now = heapq.heappop(min_)
    if now == B:
        print(cost)
        print(len(visited))
        print(*visited)
        break

    for c, next in adj[now]:
        C = cost + c
        if vi[next] > C:
            vi[next] = c
            heapq.heappush(min_, (C, visited + [next], next))
