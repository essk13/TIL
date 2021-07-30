def min_road_ladder():
    case = int(input())
    ladder = []

    # 사다리 게임판(2중 리스트) 생성
    for number in range(100):
        ladder_line = list(map(int, input().split()))
        ladder.append(ladder_line)

    x = 0
    start = 0
    start_list = []
    road_list = []

    while True:
        y = 0
        road = 0

        # 하나의 반복문은 하나의 사다리 줄
        while y < 100:
            # 시작 위치가 1이 아니면 반복문 종료
            if ladder[y][x] == 0:
                break

            elif ladder[y][x] == 1:

                # x+1이 100보다 작으면서 우측이 1인 경우 우측이 0일때까지 이동 후 아래로 1칸 이동
                if x + 1 < 100 and ladder[y][x+1] == 1:
                    while x + 1 < 100 and ladder[y][x+1] != 0:
                        x += 1
                        road += 1
                    y += 1
                    road += 1

                # x-1이 0보다 이상이면서 좌측이 1인 경우 좌측이 0일때까지 이동 후 아래로 1칸 이동
                elif x - 1 >= 0 and ladder[y][x-1] == 1:
                    while x - 1 >= 0 and ladder[y][x-1] != 0 :
                        x -= 1
                        road += 1
                    y += 1
                    road += 1
                
                else:
                    # y가 99인 경우 이동한 거리와 시작 위치를 리스트에 저장 후 반복문 종료
                    if y == 99:
                        road_list.append(road)
                        start_list.append(start)
                        break

                    # y가 99가 아닌경우 아래로 1칸 이동
                    else:
                        y += 1
                        road += 1

        # 한줄의 게임이 종료되면 시작값 +1
        start += 1
        x = start

        if start > 99:
            break

    # 시작값과 이동거리 리스트 반전(동일한 이동거리일 경우 높은 시작값을 반환하기 위함)
    start_list.reverse()
    road_list.reverse()

    # 이동거리가 최소인 값의 index 계산 및 해당 시작값 반환
    min_idx = road_list.index(min(road_list))
    min_start = start_list[min_idx]
    return min_start

case_num = 10

for case in range(case_num):
    print(f'#{case+1} {min_road_ladder()}')