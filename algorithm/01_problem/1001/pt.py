# def f(n, k):
#     '''
#     * 순열 함수 *
#     n = 순열의 길이
#     k = 결정 위치
#     '''
#     if n == k:
#         print(p)
#     else:
#         for i in range(len(arr)):
#             if u[i] == 0:
#                 u[i] = 1
#                 p[k] = arr[i]
#                 f(n, k+1)
#                 u[i] = 0


# p = [0] * 3
# arr = [1, 2, 3, 4, 5]
# u = [0] * len(arr)
# f(3, 0)

# def comb(n, r):
#     '''
#     * 조합 함수 *
#     n = 배열의 원소 수
#     r = 조합의 크기
#     '''
#     if r == 0: print(tr)
#     elif n < r: return
#     else:
#         tr[r-1] = arr[n-1]
#         comb(n-1, r-1)
#         comb(n-1, r)
#
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# tr = [0] * 3
# comb(10, 3)

######################

def nCr(n, r, s, k):
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            nCr(n, r, i+1, k+1)

comb = [0] * 3
nCr(10, 3, 0, 0)
