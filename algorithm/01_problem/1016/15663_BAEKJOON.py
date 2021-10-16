def per(lv):
    global ans
    if lv == M:
        ans.append(tuple(p))
        return
    for i in range(N):
        if u[i]:
            u[i] = 0
            p[lv] = n[i]
            per(lv+1)
            u[i] = 1


N, M = map(int, input().split())
n = list(map(int, input().split()))
n.sort()
p = [0] * M
u = [1] * N
ans = []
per(0)
ans = set(ans)
ans = list(ans)
ans.sort()
for i in range(len(ans)):
    print(*ans[i])