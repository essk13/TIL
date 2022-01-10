def dfs(m, c):
    global cost
    if m >= 11:
        cost = min(c, cost)
        return
    dfs(m + 1, c + min(plan[m+1] * D, M))
    dfs(m + 3, c + T)
    return

for tc in range(int(input())):
    D, M, T, Y = map(int, input().split())
    plan = list(map(int, input().split()))

    cost = Y
    ret = dfs(-1, 0)

    print('#{} {}'.format(tc+1, cost))