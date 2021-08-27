# def traverse(t):
#     if t:
#         preorder.append(t)
#         if visited[t] == 0:
#             visited[t] = 1
#             traverse(left[t])
#             inorder.append(t)
#             traverse(right[t])
#             postorder.append(t)
#
#
# V = 10
# E = 9
# edge = [1, 3, 1, 5, 3, 2, 3, 6, 5, 7, 5, 8, 7, 9, 8, 4, 9, 10]
# visited = [0] * 11
# root = 1
# left = [0] * 11
# right = [0] * 11
#
# for i in range(E):
#     if i % 2:
#         right[edge[i*2]] = edge[i*2+1]
#     else:
#         left[edge[i*2]] = edge[i*2+1]
#
# preorder = []
# postorder = []
# inorder  = []
#
# traverse(root)
#
# print(*preorder)
# print(*postorder)
# print(*inorder)
###################################################################


def preorder(t):
    if node[t]:
        print(node[t], end=' ')
        if visited[node[t]] == 0 and (t * 2 + 1) <= (2 ** lv - 1):
            visited[node[t]] = 1
            preorder(t*2)
            preorder(t*2+1)


V = 10
E = 9
lv = 5
edge = [1, 3, 1, 5, 3, 2, 3, 6, 5, 7, 5, 8, 7, 9, 8, 4, 9, 10]
node = [0] * (2 ** lv - 1)
visited = [0] * 11
for i in range(E):
    st, ed = edge[i*2], edge[i*2+1]
    if i == 0:
        node[1], node[2] = st, ed
    elif st in node:
        if node[(node.index(st))*2]:
            node[(node.index(st))*2+1] = ed
        else:
            node[(node.index(st))*2] = ed

preorder(1)
