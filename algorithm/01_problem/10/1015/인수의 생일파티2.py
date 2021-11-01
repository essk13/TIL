import sys
sys.stdin = open('party.txt', 'r')

import heapq

for tc in range(int(input())):
    N, M, X = map(int, input().split())
    adj1 = [[] for _ in range(N+1)]
    adj2 = [[] for _ in range(N+1)]
    for i in range(M):
        st, ed, t = map(int, input().split())
        adj1[st].append([t, ed])
        adj2[ed].append([t, st])

    min_heap = [(0, X)]
    toX = [21e8] * (N + 1)
    toX[X] = 0
    while min_heap:
        time, now = heapq.heappop(min_heap)

        for t, nt in adj1[now]:
            if toX[nt] > time + t:
                toX[nt] = time + t
                heapq.heappush(min_heap, (time+t, nt))

    min_heap = [(0, X)]
    back = [21e8] * (N + 1)
    back[X] = 0
    while min_heap:
        time, now = heapq.heappop(min_heap)

        for t, nt in adj2[now]:
            if back[nt] > time + t:
                back[nt] = time + t
                heapq.heappush(min_heap, (time+t, nt))

    ans = 0
    for i in range(1, N+1):
        ans = max(ans, back[i] + toX[i])
    print('#{} {}'.format(tc+1, ans))

#1 10
#2 213
#3 99
#4 253
#5 330
#6 294
#7 305
#8 346
#9 210
#10 50534
