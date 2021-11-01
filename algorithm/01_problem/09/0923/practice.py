# def mid(node):
#     if len(tree[node]) == 0:
#         print(node, end=' ')
#         return
#     for i in range(len(tree[node])):
#         mid(tree[node][i])
#         if i == 0:
#             print(node, end=' ')
#
#
# tree = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
#     [7, 8],
#     [],
#     [],
#     [],
#     [],
#     [],
# ]
#
# mid(0)
##########################################################
# def dfs(now):
#     if now == -1 : return
#     dfs(left[now])  # left subtree
#     print(now, end=' ')
#     dfs(right[now]) # right subtree
#
#
# left = [-1 for _ in range(9)]
# right = [-1 for _ in range(9)]
# left[0] = 1
# right[0] = 2
# left[1] = 3
# right[1] = 4
# left[2] = 5
# right[2] = 6
# left[3] = 7
# right[3] = 8
#
# dfs(0)
##########################################################
# def dfs(now):
#     if now >= len(node): return
#     if node[now] == '': return
#     dfs(2*now)      # left subtree
#     print(node[now], end=' ')
#     dfs(2*now+1)    # right subtree
#
#
# node = ['', 'A', 'B', 'C', 'D', 'E', '', 'F', 'G', 'H']
# dfs(1)
##########################################################
# tree = [0]
#
# lst = [3, 2, 5, 7, 1, 0, 7]
#
# for i in range(len(lst)):
#     tree.append(lst[i])
#     now = len(tree) - 1
#     parent = now // 2
#     # min heap 유지
#     while now > 1 and tree[parent] > tree[now]:
#         tree[parent], tree[now] = tree[now], tree[parent]
#         now = parent
#         parent = now // 2
# #     while True:
# #         for j in range(1, len(tree)):
# #             if tree[j] < tree[j//2]:
# #                 tree[j], tree[j//2] = tree[j//2], tree[j]
# #                 break
# #         else:
# #             break
# #
# print(tree)
##########################################################
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    queue = deque()
    queue.append([y, x, 0])
    while queue:
        ny, nx, path = queue.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < 6 and 0 <= tx < 9:
                if MAP[ty][tx] == 'E':
                    return path + 1
                if MAP[ty][tx] == '_' and visited[ty][tx] == 0:
                    queue.append([ty, tx, path+1])


MAP = [
    "#########",
    "#S#_____#",
    "#_#_##E##",
    "#___#___#",
    "#_______#",
    "#########",
]
visited = [[0] * 9 for _ in range(6)]
visited[1][1] = 1
ans = bfs(1, 1)
print(ans)