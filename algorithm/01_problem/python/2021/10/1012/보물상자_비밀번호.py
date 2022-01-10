for tc in range(int(input())):
    N, K = map(int, input().split())
    lst = list(input())
    len_pw = N // 4
    pw_lst = set()
    for i in range(N):
        cnt = 0
        pw = ''
        while cnt < len_pw:
            pw += lst[i]
            cnt += 1
            i += 1
            if i >= N:
                i = 0

        pw_lst.add(int(pw, 16))

    pw_lst = list(pw_lst)
    pw_lst.sort(reverse=True)
    print('#{} {}'.format(tc+1, pw_lst[K-1]))
