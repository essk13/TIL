def gravity():
    row = int(input())
    boxes = list(map(int, input().split()))

    max_gravity = 0
    for i in range(row):
        x = 0
        for j in range(i, row):
            if boxes[i] <= boxes[j]:
                x += 1
        gravity = row - i - x
        if gravity > max_gravity:
            max_gravity = gravity

    return max_gravity

test_case = int(input())

for case in range(test_case):
    print(f'#{case+1} {gravity()}')