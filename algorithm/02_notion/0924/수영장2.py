import sys
sys.stdin = open('수영장.txt', 'r')

# def check(c, m):
#     '''
#     c = 이전 까지의 요금
#     m = 현재 달
#     '''
#     global cost
#     if m > 12:
#         cost = min(cost, c)
#         return
#     check(c + (plan[m] * D), m + 1)
#     check(c + M, m + 1)
#     # check(c + min(plan[m] * D, M), m + 1)
#
#     check(c + T, m + 3)
#
#
# T = int(input())
# for tc in range(T):
#     D, M, T, Y = map(int, input().split())
#     plan = [0] + list(map(int, input().split()))
#
#     cost = Y
#     check(0, 1)
#     print('#{} {}'.format(tc+1, cost))


###############################################

T = int(input())
for tc in range(T):
    D, M, T, Y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    dp = [0] * 13

    dp[1] = min(M, plan[1] * D)
    dp[2] = dp[1] + min(M, plan[2] * D)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + T, dp[i-1] + M, dp[i-1] + (plan[i] * D))

    print('#{} {}'.format(tc + 1, min(dp[12], Y)))