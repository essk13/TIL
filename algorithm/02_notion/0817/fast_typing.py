def fast_typing():
    A, B = input().split()
    a = len(A)
    b = len(B)

    if a == 1 or b == 1:
        return a

    cnt = 0
    x = 0
    while x <= a - b:
        i = x
        for j in range(b):
            if A[i+j] != B[j]:
                x += 1
                break
        else:
            cnt += (b - 1)
            x += b

    ret = a - cnt
    return ret

T = int(input())
for tc in range(T):
    print('#{} {}'.format(tc+1, fast_typing()))


#import sys
#sys.stdin = open('input.txt', 'r')

# def is_same(start_idx, n):
#     if start_idx + n - 1 >= len(A) : return 0
#     for i in range(n) :
#         if A[start_idx +i] != B[i]:
#             return 0
#     return 1
#
# T = int(input())
# for tc in range(1, T + 1) :
#     A ,B = input().rstrip().split()
#     i = 0 # 비교시작인덱스
#     n = len(A)
#     cnt = 0 # 타이핑 횟수
#     while i < n:
#         ret = is_same(i,len(B)) # 같으면 단축키 사용
#         if ret == 1: # 단축키 사용가능
#             i += len(B)
#             cnt += 1
#         else :
#             i += 1
#             cnt += 1
#     print("#{} {}".format(tc, cnt))