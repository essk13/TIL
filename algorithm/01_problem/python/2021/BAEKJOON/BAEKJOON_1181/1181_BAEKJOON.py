import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
arr = []
for _ in range(N):
    word = input().strip()
    heapq.heappush(arr, (len(word), word))

pre = ''
while arr:
    now = heapq.heappop(arr)[1]
    if pre != now:
        print(now)
        pre = now