import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * n
dp = [0] * n
for i in range(n):
    stair[i] = int(input())

# 각 계단의 위치에 도착했을 때 가능한 최고 점수 저장
dp[0] = stair[0]
if n > 1:
    dp[1] = stair[0] + stair[1]
if n > 2:
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for j in range(3, n):
    dp[j] = max(dp[j-3] + stair[j-1] + stair[j], dp[j-2] + stair[j])

print(dp[n-1])
