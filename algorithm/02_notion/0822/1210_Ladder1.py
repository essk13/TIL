import sys
sys.stdin = open('1210.txt', 'r')

T = 10
for tc in range(T):
    case = '#' + input()
    # 인덱스 조정을 쉽게 하기위해 양쪽 끝에 0을 추가한 사다리 판 생성
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # 도착지점의 x값 확인
    for i in range(102):
        if ladder[99][i] == 2:
            x = i
            break
    y = 99
    ans = 0
    # 도착지점에서 역으로 탐색하여 출발지점 확인
    while y >= 0:
        # y가 0인 경우의 x값이 출발지점
        # 좌, 우에 0을 추가했음으로 답은 x - 1
        if y == 0:
            ans = x - 1
            break
        # 좌, 우가 0이면서 y가 0이 아닌경우 위로 이동
        while ladder[y][x+1] == 0 and ladder[y][x-1] == 0 and y != 0:
            y -= 1
        # 우측이 1인 경우 1이 아닐때까지 우측으로 이동 후 위로 1칸 이동
        if ladder[y][x+1] == 1:
            while ladder[y][x+1] == 1:
                x += 1
            y -= 1
        # 좌측이 1인 경우 1이 아닐때까지 좌측으로 이동 후 위로 1칸 이동
        elif ladder[y][x-1] == 1:
            while ladder[y][x-1] == 1:
                x -= 1
            y -= 1

    print('{} {}'.format(case, ans))