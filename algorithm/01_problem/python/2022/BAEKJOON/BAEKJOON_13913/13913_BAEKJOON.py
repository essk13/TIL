import heapq


N, K = map(int, input().split())
sp = [0] * 100001
sp[N] = 1

q = [(0, N, str(N))]

while q:
    sec, n, path = heapq.heappop(q)
    if n == K:
        print('{}\n{}'.format(sec, path))
        break

    if n - 1 >= 0 and (sp[n-1] == 0 or sp[n-1] > sec + 1):
        sp[n-1] = sec + 1
        heapq.heappush(q, (sec + 1, n - 1, path + ' ' + str(n - 1)))

    if n + 1 <= 100000 and (sp[n+1] == 0 or sp[n+1] > sec + 1):
        sp[n+1] = sec + 1
        heapq.heappush(q, (sec + 1, n + 1, path + ' ' + str(n + 1)))

    if 2 * n <= 100000 and (sp[2*n] == 0 or sp[2*n] > sec + 1):
        sp[2*n] = sec + 1
        heapq.heappush(q, (sec + 1, 2 * n, path + ' ' + str(2 * n)))
