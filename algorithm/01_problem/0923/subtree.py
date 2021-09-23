from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    cnt = 1
    while queue:
        now = queue.popleft()
        for i in range(2):
            if adj[now][i] != 0:
                queue.append(adj[now][i])
                cnt += 1
    return cnt


T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    adj = [[0, 0] for _ in range(E+2)]
    check = list(map(int, input().split()))
    for i in range(0, len(check), 2):
        if i % 2 == 0:
            if adj[check[i]][0] == 0:
                adj[check[i]][0] = check[i+1]
            else:
                adj[check[i]][1] = check[i+1]

    ans = bfs(N)
    print('#{} {}'.format(tc+1, ans))

#
# T = int(input())
#
# def dfs(now) :
#     global cnt
#     if now == 0 : return
#     cnt += 1
#     dfs(adj[now][0]) # 왼쪽 자식
#     dfs(adj[now][1]) # 오른쪽 자식
#
# for tc in range(1, T + 1) :
#     E,N = map(int ,input().split())
#     lst = list(map(int ,input().split()))
#     adj = [[0,0] for _ in range(E + 2)] # 1 ~ E+1 번 노드
#     for i in range(0,len(lst),2):
#         parent = lst[i]
#         child = lst[i + 1]
#         if adj[parent][0] == 0 :
#             adj[parent][0] = child
#         else :
#             adj[parent][1] = child
#     cnt = 0
#     dfs(N)
#     print("#{} {}".format(tc, cnt))
