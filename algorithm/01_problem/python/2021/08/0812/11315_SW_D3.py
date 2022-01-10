def omok():
    N = int(input())
    table = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            x = j
            y = i
            if table[y][j] == 'o':
                cnt = 1
                
                # 우측에 'o'가 아닐때까지 카운트
                while x + 1 < N and table[y][x+1] == 'o':
                    x += 1
                    cnt += 1
                if cnt > 4:
                    return 'YES'

                cnt = 1
                x = j
                # 아래가 'o'가 아닐때까지 카운트
                while y + 1 < N and table[y+1][x] == 'o':
                    y += 1
                    cnt += 1
                if cnt > 4:
                    return 'YES'

                cnt = 1
                y = i
                # 우하단이 'o'가 아닐때까지 카운트
                while x + 1 < N and y + 1 < N and table[y+1][x+1] == 'o':
                    x += 1
                    y += 1
                    cnt += 1
                if cnt > 4:
                    return 'YES'

                cnt = 1
                x = j
                y = i
                # 좌하단이 'o'가 아닐때까지 카운트
                while 0 <= x - 1 and y + 1 < N and table[y+1][x-1] == 'o':
                    x -= 1
                    y += 1
                    cnt += 1
                if cnt > 4:
                    return 'YES'

    return 'NO'

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, omok()))