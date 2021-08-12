def word_puzzle():
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int,input().split())) for _ in range(N)]

    t_cnt = 0
    for y in range(N):
        for i in range(N):
            cnt_x = 0
            cnt_y = 0
            x = i
            if x == 0 and puzzle[y][x] == 1 or 0 < x < N and puzzle[y][x] == 1 and puzzle[y][x-1] == 0:
                cnt_x += 1
                while x + 1 < N and puzzle[y][x+1] == 1:
                    cnt_x += 1
                    x += 1
            x = i
            if x == 0 and puzzle[x][y] == 1 or 0 < x < N and puzzle[x][y] == 1 and puzzle[x-1][y] == 0:
                cnt_y += 1
                while x + 1 < N and puzzle[x+1][y] == 1:
                    cnt_y += 1
                    x += 1

            if cnt_x == K:
                t_cnt += 1
            if cnt_y == K:
                t_cnt += 1

    return t_cnt

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, word_puzzle()))