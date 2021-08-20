# def rotate(lst):
#     a = 0
#     for i in range(len(lst) - 1, -1, -1):
#         if i == len(lst) - 1:
#             a = lst[i]
#         else:
#             lst[i + 1] = lst[i]
#     else:
#         lst[0] = a


# lst = [3, 4, 7, 9, 8, 5]
# for j in range(3):
#     rotate(lst)
#     print(lst)

# def rotate_2(arr):
#     temp = [
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]
#     ]
#
#     ln = len(arr)
#     for y in range(ln):
#         for x in range(ln):
#             temp[x][ln - 1 - y] = arr[y][x]
#
#     for y in range(ln):
#         for x in range(ln):
#             arr[y][x] = temp[y][x]
#
#
# arr = [
#     [3, 2, 1],
#     [5, 5, 5],
#     [7, 6, 5]
# ]
#
# for i in range(3):
#     rotate_2(arr)
#     for j in range(len(arr)):
#         print(arr[j])

# import time
#
#
# def map_print(y, x):
#     '''
#     @ 가 이동하는 모습 표현
#     '''
#     for i in range(100): print(end=' ')
#     print()
#     for r in range(7):
#         for c in range(10):
#             if (y, x) == (r, c):
#                 print('@', end='')
#             else:
#                 print(MAP[y][x], end='')
#         print()
#
#     time.sleep(0.7)
#
# def dfs(y, x):
#     if MAP[y][x] == '#': return
#     if visited[y][x] == '1' : return
#     visited[y][x] = 1
#     dfs(y-1, x)
#     map_print(y, x)
#     dfs(y+1, x)
#     map_print(y, x)
#     dfs(y ,x-1)
#     map_print(y, x)
#     dfs(y, x+1)
#     map_print(y, x)
#     return
#
#
# MAP = [
#     '##########',
#     '#_#___#__#',
#     '#_#_#_#_##',
#     '#_#_#_#__#',
#     '#_#_#_#_##',
#     '#___#____#',
#     '##########',
# ]
#
# visited = [[0] * 10 for _ in range(7)]
#
# dfs(1, 1)
#
# import time
#
# def map_print(ny,nx): # @
#     for i in range(100): print(end = ' ')
#     print()
#     for y in range(7):
#         for x in range(10) :
#             if (y,x) == (ny,nx):
#                 print("@",end='')
#             else :
#                 print(MAP[y][x],end ='')
#         print()
#
#     time.sleep(0.7)
#
# def dfs(y,x):
#     if MAP[y][x] == '#': return
#     if visited[y][x] == 1 : return
#     visited[y][x] = 1
#     map_print(y,x)
#     dfs(y-1,x)
#     map_print(y, x)
#     dfs(y+1,x)
#     map_print(y, x)
#     dfs(y,x-1)
#     map_print(y, x)
#     dfs(y,x+1)
#     map_print(y, x)
#     return
#
# MAP = [
#     "##########",
#     "#_#___#__#",
#     "#_#_#_#_##",
#     "#_#_#_#__#",
#     "#_#_#_#_##",
#     "#___#____#",
#     "##########",
# ]
# visited = [
#     [0 for _ in range(10)] for _ in range(7)
# ]
#
# dfs(1,1)


lst = [5, 3, 2, 7, 9, 8, 6]

for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)