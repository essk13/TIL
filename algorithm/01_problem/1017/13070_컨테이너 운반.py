for tc in range(int(input())):
    N, M = map(int, input().split())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))
    c.sort(reverse=True)
    t.sort(reverse=True)
    u = [1] * N
    ans = 0
    for i in range(M):
        for j in range(N):
            if u[j] and t[i] >= c[j]:
                ans += c[j]
                u[j] = 0
                break
    print('#{} {}'.format(tc+1, ans))