# lst = [
#     [3,2,1,5],
#     [1,2,3,4],
#     [5,4,3,2],
# ]

# de = -1

# lst[0][1], lst[2][2] = lst[2][2], lst[0][1]

# for line in range(len(lst)):
#     for x in range(len(lst[line])):
#         print(lst[line][x], end=' ')
#     print()

# for hour in range(1, 13):
#     for minute in range(1, 61):
#         print('{} 시 {} 분'.format(hour, minute))

# N = int(input())
# lst = [list(map(int,input().split())) for _ in range(N)]

# MAP = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# y = 1
# x = 1
#
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]

# for t in range(4):
#     ny = y + dy[t]
#     nx = x + dx[t]
#     if ny < 0 or nx < 0 or ny >3 or nx > 3: continue
#     print(MAP[ny][nx], end=' ')

# lst = [3,2,5]
# n = len(lst)
# for x in range(1<<n):
#     for y in range(n+1):
#         if x & (1<<y):
#             print(lst[y], end=' ')
#     print()

# bit = [0]*3
# bit_lst = []
# for x in range(2):
#     bit[0] = x
#     for y in range(2):
#         bit[1] = y
#         for z in range(2):
#             bit[2] = z
#             x = list(bit)
#             bit_lst.append(x)
#
# print(bit_lst)
#
# for k in range(len(bit_lst)):
#     for l in range(len(lst)):
#         if bit_lst[k][l] == 1:
#             print(lst[l], end=' ')
#     print()

# lst = [3,2,9,5,8,6,1]

# for i in range(len(lst)-1):
#     min_idx = i
#     min_val = 21e8
#     re_idx = 0
#     for j in range(i, len(lst)):
#         if lst[j] <= min_val:
#             min_val = lst[j]
#             re_idx = j
#     lst[i], lst[re_idx] = lst[re_idx], lst[i]

# for x in range(len(lst)):
#     for y in range(x, len(lst)):
#         if lst[x] > lst[y]:
#             lst[x], lst[y] = lst[y], lst[x]
#
# print(lst)