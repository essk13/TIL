import sys
sys.stdin = open('party.txt', 'r')

import heapq

for tc in range(int(input())):
    N, M, X = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for i in range(M):
        st, ed, t = map(int, input().split())
        adj[st].append([t, ed])

    ans = 0
    for i in range(1, N+1):
        if i != X:
            min_heap = [(0, i)]
            u = [21e8] * (N + 1)
            u[i] = 0
            toX = 21e8
            while min_heap:
                time, now = heapq.heappop(min_heap)
                if time > toX: continue
                if now == X:
                    toX = min(toX, time)
                    continue
                for t, n in adj[now]:
                    if u[n] > time + t:
                        u[n] = time + t
                        heapq.heappush(min_heap, (time + t, n))

            min_heap = [(0, X)]
            u = [21e8] * (N + 1)
            u[X] = 0
            back = 21e8
            while min_heap:
                time, now = heapq.heappop(min_heap)
                if time > back: continue
                if now == i:
                    back = min(back, time)
                    continue
                for t, n in adj[now]:
                    if u[n] > time + t:
                        u[n] = time + t
                        heapq.heappush(min_heap, (time + t, n))

            ans = max(ans, (back + toX))

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
