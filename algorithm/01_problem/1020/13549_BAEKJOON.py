import heapq

N, K = map(int, input().split())
ck = [21e8] * 100001
ck[N] = 0
min_ = [(0, N)]
while min_:
    sec, n = heapq.heappop(min_)
    if n == K:
        print(sec)
        break

    if n < K:
        if n*2 < 100001 and ck[n*2] > sec:
            ck[n*2] = sec
            heapq.heappush(min_, (sec, n * 2))
        if n+1 < 100001 and ck[n+1] > sec + 1:
            ck[n+1] = 0
            heapq.heappush(min_, (sec + 1, n + 1))

    if n-1 >= 0 and ck[n-1] > sec + 1:
        ck[n-1] = sec + 1
        heapq.heappush(min_, (sec + 1, n - 1))