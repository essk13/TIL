def min_max():
    N = int(input())
    numbers = list(map(int, input().split()))

    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if min_num > num:
            min_num = num

    return  (max_num - min_num)

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, min_max()))