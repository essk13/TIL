def per(lv, st):
    if lv == M:
        print(*p)
        return
    for i in range(st, N):
        if u[i]:
            u[i] = 0
            p[lv] = n[i]
            per(lv+1, i+1)
            u[i] = 1
    return

N, M = map(int, input().split())
n = list(range(1, N+1))
p = [0] * M
u = [1] * N
per(0, 0)
