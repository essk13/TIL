def white_red():
    cnt = 0
    for x in range(M):
        if flag[0][x] != 'W':
            cnt += 1
        if flag[-1][x] != 'R':
            cnt += 1
    return cnt


def count_change():
    for y in range(1, N - 1):
        W[y-1] = M - flag[y].count('W')
        B[y-1] = M - flag[y].count('B')
        R[y-1] = M - flag[y].count('R')


def blue():
    cnt = 21e8
    for w in range(N - 2):
        for b in range(1, N - 1 - w):
            r = N - 2 - w - b
            ret = 0
            for wi in range(w):
                ret += W[wi]
            for bi in range(w, w + b):
                ret += B[bi]
            for ri in range(w + b, w + b + r):
                ret += R[ri]

            if ret < cnt:
                cnt = ret
    return cnt


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    W = [0] * (N - 2)
    B = [0] * (N - 2)
    R = [0] * (N - 2)
    count_change()
    cnt = blue()
    cnt += white_red()

    print('#{} {}'.format(tc+1, cnt))
