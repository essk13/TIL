for tc in range(int(input())):
    N, n = input().split()
    n1 = int(n, 16)
    ans = bin(n1)
    ans = ans[2:]
    if len(ans) < len(n) * 4:
        ans = '0'*(len(n)*4 - len(ans)) + ans
    print('#{} {}'.format(tc+1, ans))