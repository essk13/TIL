def dfs(now, tree):
    for i in range(len(adj[now])):
        if len(adj[now]) == 1:
            if adj[now][0] == 0:
                print(tree)
                return
            print(tree + '-----[{}]'.format(adj[now][0]))
            return
        elif i == 0:
            dfs(adj[now][i], tree + '--+--[{}]'.format(adj[now][i]))
        elif i != len(adj[now]) - 1:
            dfs(adj[now][i], '     ' + '  +--[{}]'.format(adj[now][i]))
        else:
            dfs(adj[now][i], '     ' + '  L--[{}]'.format(adj[now][i]))
    return


root = int(input())
N = int(input())
adj = [[0] for _ in range(1001)]
for i in range(N):
    branch = list(map(int, input().split()))
    node = branch[0]
    child = branch[1:]
    adj[node] = child

dfs(root, '[{}]'.format(root))
