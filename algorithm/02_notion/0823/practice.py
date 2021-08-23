# lst = [1, 2, 3, 1, 2, 1, 2, 3, 1, 2]
# ans = 'O'
# # 조건이 복잡하다면 함수로 제작해서 사용
# for i in range(len(lst) - 1):
#     if lst[i] == 1 and lst[i+1] != 2:
#         ans = 'X'
#         break
#     elif lst[i] == 2 and lst[i+1] != 3:
#         ans = 'X'
#         break
#     elif lst[i] == 3 and lst[i+1] != 1:
#         ans = 'X'
#         break
#
# print(ans)

# def is_valid(left, right):
#     if left == 1 and right != 2: return False
#     if left == 2 and right != 3: return False
#     if left == 3 and right != 1: return False
#     return True
#
#
# lst = [1, 2, 3, 1, 2, 1, 2, 3, 1, 2]
#
# for i in range(len(lst) - 1):
#     ret = is_valid(lst[i], lst[i+1])
#     if not ret:
#         print('X')
#         break
# else:
#     print('O')

# def f(i, N):
#     '''
#     모든 원소를 사용해서 만드는 순열
#     '''
#     if i == N:   # 순열 완성
#         print(P)
#     else:        # i번 원소값 결정
#         for j in range(i, N):  # 자신부터 오른쪽 원소와 교환
#             P[i], P[j] = P[j], P[i]
#             f(i+1, N)
#             P[i], P[j] = P[j], P[i]
#     return
#
#
# P = [1, 2, 3]
# f(0, len(P))

#
# def f(i, N, r):
#     '''
#     원소중 r개를 이용한 순열
#     '''
#     if i == r:
#         print(P[0:r])
#     else:        # i번 원소값 결정
#         for j in range(i, N):  # 자신부터 오른쪽 원소와 교환
#             P[i], P[j] = P[j], P[i]
#             f(i+1, N, r)
#             P[i], P[j] = P[j], P[i]
#     return
#
#
# P = [1, 2, 3, 4]
# f(0, len(P), 3)
#
# import time
# import os
#
# def map_print(ny,nx,type): # @
#     os.system('cls')
#     for i in range(100): print(end = ' ')
#     print()
#     for y in range(7):
#         for x in range(10) :
#             if (ny,nx) == (y,x) and type == -1:
#                 print('X',end='')
#             elif (y,x) == (ny,nx):
#                 print("@",end='')
#             else :
#                 print(MAP[y][x],end ='')
#         print()
#
#     time.sleep(0.5)
#
#
# def dfs(y,x):
#     if MAP[y][x] == '#': map_print(y,x,-1); return         # 가지치기 (이후 재귀호출 제거)
#     if visited[y][x] == 1 : map_print(y,x,-1); return      # 가지치기 (이후 재귀호출 제거)
#     visited[y][x] = 1
#     map_print(y, x, 0)
#     dfs(y-1,x)
#     map_print(y, x, 0)
#     dfs(y+1,x)
#     map_print(y, x, 0)
#     dfs(y,x-1)
#     map_print(y, x, 0)
#     dfs(y,x+1)
#     map_print(y, x, 0)
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
#
# visited = [
#     [0 for _ in range(10)] for _ in range(7)
# ]
#
# dfs(1,1)


def dfs(level):
    # 현재 level 에서 선택할수 있는 x 좌표는 0 1 2
    if level == 3 :
        de = - 1
        return
    for x in range(3):
        if used[x] == 1 :
            continue
        MAP[level][x] = '#'
        used[x] = 1 # x좌표 사용(이후의 재귀호출에서 재사용 방지)
        dfs(level+1)
        used[x] = 0 # 원상복구
        MAP[level][x] = '_'

    return


MAP = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_'],
]
used = [0,0,0] # 0 1 2 의 사용 여부
dfs(0)