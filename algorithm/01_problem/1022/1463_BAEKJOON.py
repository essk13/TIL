import sys
I = sys.stdin.readline

N = int(I())
dp = [21e8] * (1000001)
dp[1] = 0
cnt = 0
n = 1
while n < N + 1:
    if n * 3 < 1000001 and dp[n * 3] > dp[n] + 1:
        dp[n * 3] = dp[n] + 1
    if n * 2 < 1000001 and dp[n * 2] > dp[n] + 1:
        dp[n * 2] = dp[n] + 1
    if n + 1 < 1000001 and dp[n + 1] > dp[n] + 1:
        dp[n + 1] = dp[n] + 1
    n += 1
print(dp[N])
