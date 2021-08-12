def crazy_sort2():
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(0, N - 1, 2):
        for j in range(i, N):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]

        for j2 in range(i+1, N):
            if num[i+1] > num[j2]:
                num[i+1], num[j2] = num[j2], num[i+1]

        if i == 8:
            break

    num = list(map(str, num))
    return ' '.join(num[:10])

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, crazy_sort2()))