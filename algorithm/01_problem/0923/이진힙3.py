import heapq

T = int(input())
for tc in range(T):
    pq = []
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N):
        heapq.heappush(pq, nums[i])

    ans = 0
    while N // 2 != 0:
        N //= 2
        ans += pq[N-1]
    print('#{} {}'.format(tc+1, ans))