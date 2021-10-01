for tc in range(int(input())):
    N, M = map(int, input().split())
    ans = 'OFF'
    print(M & (1 << N + 1) - 1)
    print((1 << N) - 1)
    if M & (1 << N) - 1 == (1 << N) - 1:
        ans = 'ON'
    print('#{} {}'.format(tc+1, ans))
