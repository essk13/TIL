T = int(input())
for tc in range(T):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    station = [int(input()) for _ in range(P)]

    ret = [0] * P
    for i in range(P):
        cnt = 0
        for j in range(N):
            if bus[j][0] <= station[i] <= bus[j][1]:
                cnt += 1

        ret[i] = cnt

    print('#{}'.format(tc+1), end=' ')
    print(*ret)