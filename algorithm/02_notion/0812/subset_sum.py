def subset_sum():
    A = list(range(1, 13))
    sub, total = list(map(int, input().split()))
    cnt = 0

    for i in range(1<<len(A)):
        lst = []
        for j in range(len(A)):
            if i & (1<<j):
                lst.append(A[j])
        if len(lst) == sub and sum(lst) == total:
            cnt += 1

    return cnt

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, subset_sum()))