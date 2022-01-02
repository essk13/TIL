from collections import deque


def bfs(node, lv):
    queue = deque()
    queue.append([node, lv])
    ret = True
    while queue and ret:
        now, n_lv = queue.popleft()
        for i in range(len(adj[now])):
            if visited[adj[now][i]] == 0:
                if n_lv == 1:
                    visited[adj[now][i]] = 2
                    queue.append([adj[now][i], 2])
                elif n_lv == 2:
                    visited[adj[now][i]] = 1
                    queue.append([adj[now][i], 1])
            elif visited[adj[now][i]] == n_lv:
                ret = False
            if not ret:
                break

    return ret


K = int(input())
for tc in range(K):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        st, ed = map(int, input().split())
        adj[st].append(ed)
        adj[ed].append(st)

    for x in range(1, V+1):
        if visited[x] == 0:
            visited[x] = 1
            ret = bfs(x, 1)
            if not ret:
                 break

    if ret:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)
