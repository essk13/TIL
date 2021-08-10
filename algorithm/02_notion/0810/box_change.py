test_case = int(input())

for case in range(test_case):
    N, Q = list(map(int, input().split()))
    boxes = [0] * N

    for i in range(1, Q+1):
        L, R = list(map(int, input().split()))

        for j in range(L-1, R):
            boxes[j] = i
    boxes = list(map(str, boxes))
    print('#{} {}'.format(case+1, ' '.join(boxes)))