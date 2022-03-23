def per(lv):
    global ans
    if lv == M:
        ans.append(tuple(p))
        return
    for i in range(len(n)):
        if n[i] >= p[lv-1]:
            p[lv] = n[i]
            per(lv+1)
            p[lv] = 0


N, M = map(int, input().split())
n = list(map(int, input().split()))
n.sort()
p = [0] * M
ans = []
per(0)
ans = set(ans)
ans = list(ans)
ans.sort()
for i in range(len(ans)):
    print(*ans[i])