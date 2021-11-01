import sys
sys.stdin = open('input.txt', 'r')

def dfs(node):
    if type(adj[node]) == int:
        return adj[node]
    a = int(adj[node][1])
    b = int(adj[node][2])
    c1 = dfs(a)
    c2 = dfs(b)
    p = adj[node][0]
    if p == '-':
        ret = c1 - c2
    elif p == '+':
        ret = c1 + c2
    elif p == '*':
        ret = c1 * c2
    else:
        ret = c1 / c2
    return ret

T = 10
for tc in range(T):
    N = int(input())
    adj = [[] for _ in range(N+1)]
    for i in range(N):
        put = list((input().split()))
        if len(put) == 4:
            n, p, c1, c2 = put
            adj[int(n)] = [p, c1, c2]
        else:
            n, v = put
            adj[int(n)] = int(v)

    ans = int(dfs(1))
    print('#{} {}'.format(tc+1, ans))
