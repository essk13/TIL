def f(lv, n):
    if lv == M:
        for x in p:
            if x: print(x, end=' ')
            else: break
        print()
        return
    for i in range(1, N+1):
        if i >= n:
            p[lv] = i
            f(lv+1, i)


N, M = map(int, input().split())
p = [0] * N
f(0, 0)
