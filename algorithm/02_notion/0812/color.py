def color():
    N = int(input())
    MAP = [[0]*11 for _ in range(11)]

    for n in range(N):
        min_x, min_y, max_x, max_y, color = list(map(int, input().split()))

        for r in range(min_y, max_y+1):
            for c in range(min_x, max_x+1):
                if MAP[r][c] != color:
                    MAP[r][c] += color

    cnt = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if MAP[i][j] >= 3:
                cnt += 1

    return cnt

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, color()))