n, m = map(int, input().split())
nums = list(range(1, n+1))
N = 1
for i in range(-1, -m - 1, -1):
    N *= nums[i]
M = 1
for j in range(m):
    M *= nums[j]

print(N // M)
