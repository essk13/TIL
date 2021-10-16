def per(lv, st):
    if lv == 6:
        print(*p)
        return
    for i in range(st, N):
        if u[i]:
            u[i] = 0
            p[lv] = lst[i]
            per(lv+1, i+1)
            u[i] = 1
            p[lv] = 0
    return


while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0: break
    N = lst[0]
    lst = lst[1:]
    u = [1] * N
    p = [0] * 6
    per(0, 0)
    print()