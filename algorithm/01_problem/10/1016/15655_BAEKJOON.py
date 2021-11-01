def per(lv, st):
    if lv == M:
        print(*p)
        return
    for i in range(st, N):
        if u[i]:
            u[i] = 0
            p[lv] = lst[i]
            per(lv+1, i)
            u[i] = 1


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
p = [0] * M
u = [1] * N
per(0, 0)