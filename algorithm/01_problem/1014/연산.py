from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    ck = [0] * 10000001
    ck[N] = 1
    qu = deque([[N, 0]])
    p = [1, -1, 2, -10]
    min_ = 0
    while qu:
        n, lv = qu.popleft()
        if n == M:
            min_ = lv
            break
        for j in range(4):
            if j == 2:
                na = n * p[j]
            else:
                na = n + p[j]
            if 1 <= na <= 1000000 and ck[na] == 0:
                ck[na] = 1
                qu.append([na, lv+1])

    print('#{} {}'.format(tc+1, min_))
