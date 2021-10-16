def per(lv, st):
    if lv == M:
        print(*p)
        return
    for i in range(st, N):
        p[lv] = n[i]
        per(lv+1, i)


N, M = map(int, input().split())
n = list(map(int, input().split()))
n.sort()
p = [0] * M
per(0, 0)