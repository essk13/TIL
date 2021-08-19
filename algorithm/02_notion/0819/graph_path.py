def node(S, G):
    ret = 0
    if S == G:
        return 1

    for i in range(1, V+1):
        if arr[S][i] == 1 and visited[i] == 0:
            visited[i] = 1
            ret += node(i, G)

    return ret

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    arr = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        A, B = map(int, input().split())
        arr[A][B] = 1

    S, G = map(int, input().split())
    visited[1] = 1
    ans = node(S, G)
    print('#{} {}'.format(tc+1, ans))