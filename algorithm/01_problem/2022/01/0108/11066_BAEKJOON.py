import sys
input = sys.stdin.readline

for tc in range(int(input())):
    K = int(input())
    data = list(map(int, input().split()))

    dp = [[0] * K for _ in range(K)]
    for i in range(K - 1):
        dp[i][i+1] = data[i] + data[i+1]
        for j in range(i + 2, K):
            dp[i][j] = dp[i][j-1] + data[j]

    for d in range(2, K):
        for i in range(K - d):
            j = i + d
            min_ = [dp[i][n] + dp[n+1][j] for n in range(i, j)]
            dp[i][j] += min(min_)

    print(dp[0][K-1])
