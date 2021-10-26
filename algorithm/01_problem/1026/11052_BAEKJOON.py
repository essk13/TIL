import sys
I = sys.stdin.readline

N = int(I())
card_pack = [0] + list(map(int, I().split()))
dp = [0] * (N+1)
dp[1] = card_pack[1]
dp[2] = max(dp[1] * 2, card_pack[2])

card = 3
while card <= N:
    dp[card] = card_pack[card]
    for i in range(1, card // 2 + 1):
        dp[card] = max(dp[card], dp[i] + dp[card-i])
    card += 1

print(dp[N])
