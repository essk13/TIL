for tc in range(int(input())):
    N, M = map(int, input().split())
    M = bin(M)[2:]
    ans = 'ON'
    for i in range(len(M)-1, len(M)-N-1, -1):
        if i < 0:
            ans = 'OFF'
            break
        elif M[i] == '0':
            ans='OFF'
            break
    print('#{} {}'.format(tc+1, ans))
