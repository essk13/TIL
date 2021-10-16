def per(lv):
    if lv == N:
        print(*p)
        return
    for i in range(N):
        if u[i]:
            u[i] = 0
            p[lv] = lst[i]
            per(lv+1)
            u[i] = 1
            p[lv] = 0
    return

N = int(input())
lst = list(range(1, N+1))
p = [0] * N
u = [1] * N
per(0)