def f(lv):
    if lv == M:
        print(*p)
        return
    for i in range(1, N + 1):
        if u[i] == 0:
            u[i] = 1
            p[lv] = i
            f(lv + 1)
            u[i] = 0


N, M = map(int, input().split())
p = [0] * M
u = [0] * (N + 1)
f(0)
