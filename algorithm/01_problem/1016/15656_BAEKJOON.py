def per(lv):
    if lv == M:
        print(*p)
        return
    for i in range(N):
        p[lv] = lst[i]
        per(lv+1)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
p = [0] * M
per(0)