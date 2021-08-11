def subset_sum():
    N = int(input())
    numbers = list(map(int, input().split()))

    subset = []
    cnt = 0
    for x in range(1<<N):
        for y in range(N+1):
            if x & (1<<y):
                subset.append(numbers[y])
        if len(subset) == 0 or sum(subset) == 0:
            cnt += 1
        subset = []

    return cnt

test_case = 10

for case in range(test_case):
    print('#{} {}'.format(case+1, subset_sum()))