import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = wine[0]
if n > 1:
    dp[1] = dp[0] + wine[1]
    if n > 2:
        dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])

print(max(dp))
