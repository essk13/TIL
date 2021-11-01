for tc in range(int(input())):
    N = float(input())
    ans = ''
    print('#{}'.format(tc + 1), end=' ')
    while N:
        N *= 2
        if N >= 1:
            ans += '1'
            N -= 1
        else:
            ans += '0'
        if len(ans) > 12:
            print('overflow')
            break
    else:
        print(ans)
