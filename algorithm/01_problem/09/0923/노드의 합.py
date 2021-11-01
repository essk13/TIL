T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    adj = [0 for _ in range(N+1)]
    for i in range(M):
        n, x = map(int, input().split())
        adj[n] = x

    print('#{}'.format(tc+1), end=' ')
    for j in range(N, -1, -1):
        if j % 2 == 0:
            if j+1 <= N:
                adj[j//2] = adj[j] + adj[j+1]
            else:
                adj[j//2] = adj[j]
            if j // 2 == L:
                print(adj[L])
                break
################################################
# def dfs(idx) :
#     if idx > N : return
#     if tree[idx] > 0 : return
#     dfs(idx * 2) # left subtree 값 채우기
#     dfs(idx * 2 + 1) # right subtree 값 채우기
#
#     # tree[idx]= tree[idx * 2 ] + tree[idx * 2 + 1]
#     if idx * 2 <= N : tree[idx] += tree[idx * 2]
#     if idx * 2 + 1 <= N : tree[idx] += tree[idx * 2 + 1]
#
#
# T = int(input())
# for tc in range(1, T + 1) :
#     N,M,L = map(int, input().split())
#     tree = [0] * (N + 1)
#     for i in range(M):
#         a,b = map(int, input().split())
#         tree[a] = b
#
#     dfs(1)
#     print("#{} {}".format(tc, tree[L]))
################################################
# def dfs(idx) :
#     if idx > N : return 0
#     if tree[idx] > 0 : return tree[idx]
#     a = dfs(idx * 2) # left subtree 값 채우기
#     b = dfs(idx * 2 + 1) # right subtree 값 채우기
#     tree[idx] = a + b
#     return tree[idx]
#
#
# T = int(input())
# for tc in range(1, T + 1) :
#     N,M,L = map(int, input().split())
#     tree = [0] * (N + 1)
#     for i in range(M):
#         a,b = map(int, input().split())
#         tree[a] = b
#
#     dfs(1)
#     print("#{} {}".format(tc, tree[L]))
################################################
