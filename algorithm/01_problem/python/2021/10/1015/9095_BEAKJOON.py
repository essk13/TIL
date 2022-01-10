def my_sum(n, now):
    cnt = 0
    if n == now: return 1
    if n < now: return 0
    cnt += my_sum(n, now+1)
    cnt += my_sum(n, now+2)
    cnt += my_sum(n, now+3)
    return cnt

N = int(input())
nums = [int(input()) for _ in range(N)]
for i in range(N):
    ans = my_sum(nums[i], 0)
    print(ans)
