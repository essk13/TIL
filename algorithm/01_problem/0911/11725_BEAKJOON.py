from collections import deque


def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        for i in range(len(adj[now])):
            if tree[adj[now][i]] == 0:
                tree[adj[now][i]] = now
                queue.append(adj[now][i])
    return


N = int(input())
tree = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
for i in range(N-1):
    st, ed = map(int, input().split())
    if st == 1:
        adj[1].append(ed)
    elif ed == 1:
        adj[1].append(st)
    else:
        adj[st].append(ed)
        adj[ed].append(st)

bfs()

for j in range(2, N+1):
    print(tree[j])
