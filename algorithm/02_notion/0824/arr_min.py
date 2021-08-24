def arr_sum(y, total):
    global min_sum
    if y == N - 1:
        if total < min_sum:
            min_sum = total
            return
        else:
            return
    if total >= min_sum:
        return
    for i in range(N):
        if used_x[i] == 0 and y < N - 1:
            used_x[i] = 1
            arr_sum(y+1, total + MAP[y+1][i])
            used_x[i] = 0
    return


T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used_x = [0] * N
    min_sum = 21e8
    arr_sum(-1, 0)

    print('#{} {}'.format(tc+1, min_sum))