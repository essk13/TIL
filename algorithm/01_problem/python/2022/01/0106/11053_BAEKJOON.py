import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    for j in range(i):
        '''
        1) 현재 값(arr[i])가 이전 값(arr[j])보다 크면서 현재 DP(dp[i])가 이전 DP(dp[j]) 보다 작은 경우
            >> 현재 DP는 이전 DP + 1
        2) 1번과 같은 경우가 없는 경우
            >> 현재 DP = 1
        '''
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
