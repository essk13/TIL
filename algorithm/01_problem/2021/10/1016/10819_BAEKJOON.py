def per(lv):
    global ans
    if lv == N:
        ret = 0
        for j in range(N-1):
            ret += abs(p[j]-p[j+1])
        ans = max(ans, ret)
        return
    for i in range(N):
        if u[i]:
            u[i] = 0
            p[lv] = arr[i]
            per(lv+1)
            u[i] = 1
    return

N = int(input())
arr = list(map(int, input().split()))
p = [0] * N
u = [1] * N
ans = 0
per(0)
print(ans)
