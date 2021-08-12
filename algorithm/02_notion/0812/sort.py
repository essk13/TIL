def selection_sort():
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i, N):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]

    num = list(map(str, num))
    return ' '.join(num)

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, selection_sort()))