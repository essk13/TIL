def m_cost(lv, n_cost):
    global cost
    if lv == N:
        cost = min(cost, n_cost)
        return
    if n_cost >= cost: return

    for i in range(N):
        if ck[i]:
            ck[i] = 0
            m_cost(lv+1, n_cost + adj[lv][i])
            ck[i] = 1
    return


for tc in range(int(input())):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    ck = [1] * N
    cost = 21e8
    m_cost(0, 0)
    print('#{} {}'.format(tc+1, cost))
