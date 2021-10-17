def cart(n, lv, total):
    global ans
    if lv == N-1:
        ans = min(ans, total + adj[n][0])
        return
    for i in range(N):
        if u[i] and adj[n][i]:
            u[i] = 0
            cart(i, lv+1, total + adj[n][i])
            u[i] = 1


for tc in range(int(input())):
    N = int(input())
    adj = [list(map(int,input().split())) for _ in range(N)]
    u = [1] * N
    u[0] = 0
    ans = 21e8
    cart(0, 0, 0)
    print('#{} {}'.format(tc+1, ans))