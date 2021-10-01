for tc in range(int(input())):
    N, M = map(int, input().split())
    m = str(bin(M))[2:]
    ans = 'ON'
    if len(m) < N:
        ans = 'OFF'
    elif '1'*N != m[-N:]:
        ans = 'OFF'

    print('#{} {}'.format(tc+1, ans))