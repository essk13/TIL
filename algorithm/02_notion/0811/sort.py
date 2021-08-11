def selection_sort():
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1):
        for j in range(i, N):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers = list(map(str, numbers))
    return ' '.join(numbers)

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, selection_sort()))