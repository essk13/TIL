import heapq

min_heap = [1]
ugly = [0] * 1501
t = 1
pre = 0
while t < 1501:
    n = heapq.heappop(min_heap)
    if n == pre: continue
    pre = n
    ugly[t] = n
    t += 1
    heapq.heappush(min_heap, n * 2)
    heapq.heappush(min_heap, n * 3)
    heapq.heappush(min_heap, n * 5)

print(ugly)
