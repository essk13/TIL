# from collections import deque
#
# adj =[
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1],
# ]
#
# road = [1, 2, 3, 4, 5, 6, 7]
# queue = deque()
# visited = [0]*8
# queue.append(1)
# visited[1] = 1
#
#
# while queue:
#     V = queue.popleft()
#     if V == 1:
#         print(V, 'lv{}'.format(visited[V]))
#     for x in range(1, 8):
#         if adj[V][x] == 1 and visited[x] == 0:
#             visited[x] = visited[V] + 1
#             queue.append(x)
#             print(x, 'lv{}'.format(visited[x]))


# arr = [
#     [3, 2, 1, 7],
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [1, 1, 1, 1]
# ]
#
# dy = [-1, -1, 1, 1]
# dx = [-1, 1, -1, 1]
#
# lst = []
# y, x = 1, 3
#
# for i in range(4):
#     if 0 <= y + dy[i] < 4 and 0 <= x + dx[i] < 4:
#         lst.append(arr[y+dy[i]][x+dx[i]])
#
# print(max(lst))


from collections import deque

farm = [[0] * 5 for _ in range(3)]

farm[0][0] = 1
farm[2][3] = 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

queue = deque()
queue.append((0, 0))
queue.append((2, 3))

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 3 and 0 <= nx < 5:
            if farm[ny][nx] == 0:
                farm[ny][nx] = farm[y][x] + 1
                queue.append((ny, nx))
    if not queue:
        print(farm[y][x])
