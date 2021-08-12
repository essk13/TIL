def restoration():
    origin = list(map(int, list(input())))
    # length = len(origin)
    x = 1
    cnt = 0
    for idx in range(len(origin)):
        result = False

        # 원본데이터 값이 x와 일치하면 cnt += 1
        if origin[idx] == x:
            cnt += 1
            result = True

        # cnt += 1을 했을 경우 x -= 1
        if result == True:
            x -= 1
        # x가 0보다 작아지면 1로 초기화
        if x < 0:
            x = 1

    return cnt

test_case = int(input())
for case in range(test_case):
    print('#{} {}'.format(case+1, restoration()))