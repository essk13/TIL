def delta():
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    sum = 0
    for y in range(N):
        for x in range(N):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                    continue
                result = abs(lst[y][x] - lst[ny][nx])
                sum += result

    return sum

test_case = 10

for case in range(test_case):
    print('#{} {}'.format(case + 1, delta()))
