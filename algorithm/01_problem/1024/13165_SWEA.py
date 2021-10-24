import sys
sys.stdin = open('13165.txt', 'r')

import heapq

for tc in range(int(input())):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for i in range(E):
        st, ed, length = map(int, input().split())
        adj[st].append([length, ed])

    min_ = [(0, 0)]
    ans = 0
    while min_:
        L, now = heapq.heappop(min_)
        if now == N:
            ans = L
            break
        for l, to in adj[now]:
            heapq.heappush(min_,(L + l, to))
    print('#{} {}'.format(tc+1, ans))

#1 2
#2 4
#3 10