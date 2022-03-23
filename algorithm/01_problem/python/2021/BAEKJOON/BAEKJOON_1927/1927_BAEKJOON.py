import sys, heapq
input = sys.stdin.readline


N = int(input())
min_heap = []
for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(min_heap, num)

    else:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
