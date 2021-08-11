test_case = int(input())

for case in range(test_case):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    snail[0][0] = '1'
    num = 2

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x = y = i = 0
    while num <= N**2:
        if 0<=x + dx[i]<N and 0<=y + dy[i]<N and snail[y+dy[i]][x+dx[i]] == 0:
            x += dx[i]
            y += dy[i]
            snail[y][x] = str(num)
            num += 1

        else:
            i += 1
            if i > 3:
                i = 0

    print('#{}'.format(case+1))
    for line in snail:
        print(' '.join(line))