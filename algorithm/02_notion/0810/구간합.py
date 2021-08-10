def interval_cal():
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_sum = 0
    min_sum = 21e8
    for i in range(N-M+1):
        sum_val = 0
        for j in range(M):
            sum_val += numbers[i+j]
        if sum_val > max_sum:
            max_sum = sum_val
        if sum_val < min_sum:
            min_sum = sum_val

    return (max_sum - min_sum)

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, interval_cal()))