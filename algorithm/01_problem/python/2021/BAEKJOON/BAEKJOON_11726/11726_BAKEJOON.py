import sys
I = sys.stdin.readline


N = int(I())
memo = [0] * (1001)
memo[1], memo[2] = 1, 2
n = 3
while n <= N:
    memo[n] = memo[n-1] + memo[n-2]
    n += 1
ans = memo[N] % 10007
print(ans)