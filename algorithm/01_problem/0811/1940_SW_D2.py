def rc_car():
    N = int(input())
    command = [list(map(int, input().split())) for _ in range(N)]

    spd = 0
    move = 0
    for cmd in command:

        # cmd가 1인 경우 증속
        if cmd[0] == 1:
            spd += cmd[1]

        # cmd가 2인 경우 감속
        elif cmd[0] == 2:
            spd -= cmd[1]

            # 속도가 0 이하로 떨어지면 0으로 초기화
            if spd < 0:
                spd = 0

        move += spd

    return move

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, rc_car()))