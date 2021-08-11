def max_sum():
    case = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]

    max_sum = -21e8
    for y in range(100):
        sum_r = 0
        sum_c = 0
        sum_b = 0
        for x in range(100):
            sum_r += numbers[y][x]
            sum_c += numbers[x][y]
            if x == y:
                sum_b += numbers[y][x]

        if sum_r > max_sum:
            max_sum = sum_r
        if sum_c > max_sum:
            max_sum = sum_c
        if sum_b > max_sum:
            max_sum = sum_b

    i = sum_t = 0
    j = 99
    while i <= 99:
        sum_t += numbers[i][j]
        i += 1
        j -= 1

    if sum_t > max_sum:
        max_sum = sum_t

    print('#{} {}'.format(case, max_sum))

test_case = 10

for case in range(test_case):
    result = max_sum()