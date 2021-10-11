import sys
import heapq

l_heap = []
r_heap = []
N = int(input())
for n in range(N):
    num = int(sys.stdin.readline())

    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, (-num, num))
    else:
        heapq.heappush(r_heap, (num, num))

    if r_heap and l_heap[0][1] > r_heap[0][1]:
        l_max = heapq.heappop(l_heap)[1]
        r_min = heapq.heappop(r_heap)[1]
        heapq.heappush(l_heap, (-r_min, r_min))
        heapq.heappush(r_heap, (l_max, l_max))

    print(l_heap[0][1])
