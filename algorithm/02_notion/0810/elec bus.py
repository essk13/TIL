def bus_station():
    K, N, M = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    station = [0] * (N + 1)
    # for idx in range(M):
    #     station[M_list[idx]] = 1

    for m in M_list:
        station[m] = 1

    st = 0
    ch = 0
    while True:
        next_st = station[st+1:st+1+K]
        for i in range(K-1, -1, -1):
            if next_st[i] == 1:
                st += i + 1
                ch += 1
                break
        else:
            return 0

        if N - K <= st <= N:
            break

    return ch

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, bus_station()))