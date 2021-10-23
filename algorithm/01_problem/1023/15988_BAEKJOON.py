import sys
I = sys.stdin.readline

memo = [0] * 1000001
memo[1], memo[2], memo[3] = 1, 2, 4
i = 4
for i in range(4, 1000001):
    memo[i] = memo[i-1] % 1000000009 + memo[i-2] % 1000000009 + memo[i-3] % 1000000009

for tc in range(int(I())):
    n = int(I())
    print(memo[n] % 1000000009)
