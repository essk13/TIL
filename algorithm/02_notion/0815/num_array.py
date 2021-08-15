def turn(n, arr):
    for i in range(n):
        for j in range(n):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    return arr

T = int(input())

for tc in range(T):
    N = int(input())
    arr_o = [list(map(int, input().split())) for _ in range(N)]
    n_arr = [0]*N*3

    for y in range(3):
        ret = turn(N, arr_o)
        for x in range(N):
            n_arr[x+(y*N)] = list(map(str, ret[x][::-1]))
            arr_o[x] = ret[x][::-1]

    print('#{}'.format(tc+1))
    for i in range(N):
        print(''.join(n_arr[i]), end=' ')
        print(''.join(n_arr[i+N]), end=' ')
        print(''.join(n_arr[i+(2*N)]))