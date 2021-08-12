# def binary_search(lst, st, ed, mid, key):
#     if lst[mid] == key:
#         return '찾았다'
#     elif lst[st] > key or lst[ed] < key:
#         return '못찾았다'
#     elif lst[mid] < key:
#         st_r = mid
#         mid_r = int((st_r + ed) / 2)
#         binary_search(lst, st_r, ed, mid_r, key)
#     elif lst[mid] > key:
#         ed_r = mid
#         mid_r = int((st + ed_r) / 2)
#         binary_search(lst, st, ed_r, mid_r, key)
#     else:
#         return '못찾았다'
#
#
# arr = [1,2,5,7,9,15,17]
#
# l = 0
# r = len(arr) - 1
# m = int((l + r) / 2)
#
# result = binary_search(arr, l, r, m, 2)
#
# print(result)


# zone = [3, 2, 7, 5, 9, 8, 7, 2, 1]
# max_sum = 0
# idx = 0
# for x in range(len(zone) - M + 1):
#     sum_M = 0
#     for y in range(x, x + M):
#         sum_M += zone[y]
#     if sum_M > max_sum:
#         max_sum = sum_M
#         idx = x
#
# print(max_sum, idx)


# def get_sum(start_idx, M):
#     sum = 0
#     for i in range(M): # [start_idx+ 0 1 2 3 .... M-1]
#         sum += lst[start_idx + i]
#
#     return sum
#
# lst = [3,2,7,5,9,8,7,2,1]
#
# N = 9 # lst 크기
# M = int(input())
# max_idx = -1
# max_sum = int(-21e8)
# for i in range(0,N - M + 1):
#     ret = get_sum(i,M)
#     if ret > max_sum:
#         max_sum = ret
#         max_idx = i # 시작인덱스
#
# print(max_idx , max_sum)


# lst = [5, 2, 0, 7, 7, 0, 2, 1, 9]
#
# x = 0
# for j in range(len(lst)):
#     sq = []
#     x = j
#     if lst[j] != 0:
#         sq.append(lst[j])
#         if len(sq) == 1:
#             print(*sq)
#         while x + 1 < len(lst) and lst[x+1] != 0:
#             x += 1
#             sq.append(lst[x])
#             if len(sq) > 1:
#                 print(*sq


# lst = [5,2,0,7,7,0,2,1,9]
#
# def is_zero_exist(s, e):
#     for i in range(s, e + 1):
#         if lst[i] == 0 :
#             return True # 0이 있다
#
#     return False # 0이 없다
#
# for s in range(9):
#     for e in range(s,9):
#         # 1. 시작 ~ 끝 0 이있는가?
#         check = is_zero_exist(s,e)
#         # 2. 0 이 없으면 출력하기
#         if check == 0 :
#             for i in range(s, e + 1) :
#                 print(lst[i] , end = ' ')
#             print()

ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(5)]

for i in range(5):
    print(*ladder[i])