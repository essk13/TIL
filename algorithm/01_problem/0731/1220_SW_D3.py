def count_deadlock():
    '''
    주어진 자석 판에서 발생한 교착상태의 수를 반환하는 함수
    '''
    size = int(input())
    magnetics = []
    for num in range(size):
        magnetics_line = list(map(int, input().split()))
        magnetics.append(magnetics_line)

    n = 0
    deadlock = 0
    while n <= size:
        for x in range(size):
            for y in range(size):

                # 자석판 좌표에 자성체가 없는 경우
                if magnetics[y][x] == 0:
                    pass

                # 자석판 좌표에 N극 자성체가 있는 경우
                elif magnetics[y][x] == 1:
                    if y + 1 > 99:          # 좌석판을 벗어나면 제거
                        magnetics[y][x] = 0
                    elif n == size and magnetics[y+1][x] == 2:          # S극 자성체와 만나면 정지 및 교착상태 += 1
                        deadlock += 1
                    elif magnetics[y+1][x] == 0:            # 아래가 비어있으면 아래로 한칸 이동
                        magnetics[y][x], magnetics[y+1][x] = magnetics[y+1][x], magnetics[y][x]
                    else:
                        pass

                # 자석판 좌표에 N극 자성체가 있는 경우
                elif magnetics[y][x] == 2:
                    if y - 1 < 0:           # 자석판을 벗어나면 제거
                        magnetics[y][x] = 0
                    # magentics[y][x] == 1 이면서 magentics[y+1][x] == 2 인 경우에 deadlock += 1을 하지 않으면 여기서 아래 코드 실행
                    # elif n == size and magnetics[y-1][x] == 1:
                    #     deadlock += 1
                    elif magnetics[y-1][x] == 0:            # 위에가 비어있으면 위로 한칸 이동
                        magnetics[y][x], magnetics[y-1][x] = magnetics[y-1][x], magnetics[y][x]
                    else:
                        pass

        n += 1

    return deadlock

case_num = 10

for case in range(case_num):
    print(f'#{case+1} {count_deadlock()}')