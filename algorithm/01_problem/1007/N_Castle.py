def castle(y):
    cnt = 0
    if y == N - 1:
        return 1

    for i in range(N):
        if ck[i] == 1: continue
        else:
            ck[i] = 1
            cnt += castle(y + 1)
            ck[i] = 0
    return cnt


for tc in range(10):
    N = int(input())
    ck = [0] * N
    cnt = castle(0)
    print('#{} {}'.format(tc+1, cnt))
