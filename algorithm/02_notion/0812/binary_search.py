def binary_search():
    P, A, B = list(map(int, input().split()))

    total = list(range(P+1))
    st_a = st_b = 1
    ed_a = ed_b = P
    mid_a = mid_b = int((st_a + ed_a) / 2)

    cnt_a = cnt_b = 0

    if A > P and B > P:
        return 0
    elif A > P:
        return 'B'
    elif B > P:
        return 'A'

    while True:
        # mid_a = int((st_a + ed_a) / 2)
        # mid_b = int((st_b + ed_b) / 2)
        if total[mid_a] == A:
            cnt_a = 1
        elif total[mid_a] < A:
            st_a = mid_a
            mid_a = int((st_a + ed_a) / 2)
        elif total[mid_a] > A:
            ed_a = mid_a
            mid_a = int((st_a + ed_a) / 2)

        if total[mid_b] == B:
            cnt_b = 1
        elif total[mid_b] < B:
            st_b = mid_b
            mid_b = int((st_b + ed_b) / 2)
        elif total[mid_b] > B:
            ed_b = mid_b
            mid_b = int((st_b + ed_b) / 2)

        if cnt_a != 0 or cnt_b != 0:
            if cnt_a == cnt_b:
                return 0
            elif cnt_a == 1:
                return 'A'
            else:
                return 'B'

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, binary_search()))


# def b_search(left, right, target):
#     cnt = 0 # return 값
#     while left < right:
#         cnt += 1
#         mid = (left + right) // 2
#         if mid == target :
#             return cnt
#         if mid < target : # left [left=]mid target right
#             left = mid
#         elif target < mid: # left  target   [right=]mid   right
#             right = mid
#
#
# T = int(input())
# for tc in range(1, T + 1) :
#     P,Pa,Pb = map(int, input().split())
#     cnt_a = b_search(1,P,Pa) # left, right, target
#     cnt_b = b_search(1,P,Pb)
#     if cnt_a > cnt_b :
#         print("#{} A".format(tc))
#     elif cnt_b > cnt_a :
#         print("#{} B".format(tc))
#     else :
#         print("#{} 0".format(tc))