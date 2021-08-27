import sys
sys.stdin = open('fish.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()
    ans = 'Possible'
    for c in range(N):
        fish = ((customer[c] // M) * K) - (c + 1)
        if fish < 0:
            ans = 'Impossible'
    print('#{} {}'.format(tc+1, ans))
