# def walk(n):
#     if n == len(arr) - 1:
#         print(arr[n], end=' ')
#     else:
#         print(arr[n], end=' ')
#         walk(n+1)
#         print(arr[n], end=' ')
#
# arr = [3, 5, 7, 9, 10, 6]
#
# walk(0)

# def func(level):
#     if level == 3:
#         return
#     print('#',end='')
#     func(level+1)
#     func(level+1)
#     print('@', end='')
#     return
#
# func(0)

# def func(level):
#     global a
#     if level == 3:
#         print(a,end=' ')
#         a += 1
#         return
#     func(level+1)
#     func(level+1)
#     return
#
# a = 1
# func(0)

# def func(num, root):
#     if num == 2:
#         print(root, end=' ')
#         return
#
#     func(num + 1, root + 'l')
#     func(num + 1, root + 'm')
#     func(num + 1, root + 'r')
#     return
#
# func(0, '')

# def func(num, root):
#     global cnt
#     if num == 3:
#         print(root, end=' ')
#         cnt += 1
#         return
#
#     func(num + 1, root + '1')
#     func(num + 1, root + '2')
#     func(num + 1, root + '3')
#     return
#
# cnt = 0
# func(0, '')
# print('\n{}'.format(cnt))

# def dice(level, path):
#     global N
#     if level == N:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         dice(level + 1, path + str(i))
#
#     return
#
#
# N = int(input())
# dice(0, '')

# def range_sum(n):
#     if n == 1:
#         return 1
#     ret = n + range_sum(n-1)
#     return ret
#
# print(range_sum(int(input())))

# def child(n):
#
#     for i in range(8):
#         if arr[n][i] == 1:
#             child(i)
#
#     print(n, end=' ')
#     return
#
# E = 7
# arr = [[0]*8 for _ in range(8)]
# for i in range(E):
#     A, B = map(int, input().split())
#     arr[A][B] = 1
#
# node = int(input())
# child(node)

adj = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
]


def dfs(now):
    for next in range(4):
        if adj[now][next] == 1 and visited[next] == 0:  # 연결? 방문안함?
            visited[next] = 1  # 다시 재귀호출 방지
            dfs(next)

    return


visited = [0, 0, 0, 0]
visited[0] = 1  # 시작노드 0번 방문체크 (다시 재귀호출 방지가능)
dfs(0)
de = -1