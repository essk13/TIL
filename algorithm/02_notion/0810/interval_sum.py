def interval_cal():
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sum_lst = []
    for i in range(len(numbers)):
        if i == 0:
            sum_lst.append(numbers[i])
        else:
            sum_lst.append(numbers[i] + sum_lst[i - 1])

    max_sum = 0
    min_sum = 21e8
    for j in range(N-1, M-2, -1):
        if j-M >= 0:
            result = sum_lst[j] - sum_lst[j-M]
        else:
            result = sum_lst[j]
        if result > max_sum:
            max_sum = result
        if result < min_sum:
            min_sum = result

    return (max_sum - min_sum)

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, interval_cal()))