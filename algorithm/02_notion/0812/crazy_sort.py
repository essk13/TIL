def crazy_sort():
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i, N):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]

    tmp = []
    while len(num) > 0 and len(tmp) < 10:
        tmp.append(str(num.pop(len(num)-1)))
        if len(num) == 0 or len(tmp) == 10:
            break
        tmp.append(str(num.pop(0)))

    return ' '.join(tmp)

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, crazy_sort()))