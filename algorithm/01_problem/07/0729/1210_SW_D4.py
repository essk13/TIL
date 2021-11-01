def ladder():
    '''
    사다리 타기 게임 중 당첨에 도달하는
    출발 지점 계산 함수
    '''
    case = int(input())
    ladder = []

    # 사다리 게임판 2중 리스트 생성
    for n in range(100):
        ladder_line = list(map(int, input().split()))
        ladder.append(ladder_line)

    x = 0
    y = 0
    start = 0
    while True:
        x = start
        y = 0

        while y <= 99:
            # 시작값([y][start])이 0이면 break
            if ladder[y][x] == 0:
                break

            # 시작값([y][start])이 1이면 게임 시작
            elif ladder[y][x] == 1:

                # 우측에 1이 있으면서 x+1이 99를 넘지 않는 경우
                if x + 1 <= 99 and ladder[y][x+1] == 1:
                    # 우측에 0을 만날 때 까지 우측으로 이동 후 아래로 1칸
                    while x + 1 <= 99 and ladder[y][x+1] != 0:
                        x += 1
                    y += 1

                # 좌측에 1이 있으면서 x-1이 0보다 작지 않은 경우
                elif x - 1 >= 0 and ladder[y][x-1] == 1:
                    # 좌측에 0을 만날 때 까지 좌측으로 이동 후 아래로 1칸
                    while x - 1 >= 0 and ladder[y][x-1] != 0:
                        x -= 1
                    y += 1

                # 좌우가 0인 경우
                else:
                    # y가 99면 break
                    if y == 99:
                        break
                    # 그 외 아래로 1칸
                    else:
                        y += 1
            
            # 도착점의 값이 2인 경우 시작값 리턴
            elif ladder[y][x] == 2:
                return start

        start += 1

        # 혹시 start 값이 99보다 크면 Error 발생
        if start > 99:
            return 'Error'



case_num = 10

for case in range(case_num):
    print(f'#{case+1} {ladder()}')