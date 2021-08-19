# def paper(n):
#     global cnt
#     A1 = 10
#     A2 = 20
#     B = 20
#     if n == N:
#         cnt += 1
#         return
#     elif n > N:
#         return
#
#     paper(n+A1)
#     paper(n+A2)
#     paper(n+B)
#
#     return
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     cnt = 0
#     paper(0)
#     print('#{} {}'.format(tc+1, cnt))

def paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    A = 10
    B = 20
    ret = paper(N - A) + (paper(N - B) * 2)
    return ret

T = int(input())
for tc in range(T):
    N = int(input())
    print('#{} {}'.format(tc+1, paper(N)))