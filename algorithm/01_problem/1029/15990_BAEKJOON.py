import sys
I = sys.stdin.readline

def mod(n):
    return n % M


N = 100000
M = 1000000009
dp = [[0] * 4 for _ in range(N + 1)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, N + 1):
    dp[i][1] = dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-2][1] + dp[i-2][3]
    dp[i][3] = dp[i-3][1] + dp[i-3][2]

    for j in range(1, 4):
        dp[i][j] = mod(dp[i][j])

T = int(I())
ans = [0] * T
for tc in range(T):
    ans[tc] = sum(dp[int(I())]) % M

print('\n'.join(map(str, ans)))
