import sys, heapq
input = sys.stdin.readline


N = int(input())
max_heap = []
for _ in range(N):
    num = int(input())
    if num:
        heapq.heappush(max_heap, (-num, num))

    else:
        if max_heap:
            print(heapq.heappop(max_heap)[1])
        else:
            print(0)
