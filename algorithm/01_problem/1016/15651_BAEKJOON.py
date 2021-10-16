def per(lv):
    if lv == M:
        print(*p)
        return
    for i in range(N):
        p[lv] = n[i]
        per(lv+1)


N, M = map(int, input().split())
n = list(range(1, N+1))
p = [0] * M
per(0)
