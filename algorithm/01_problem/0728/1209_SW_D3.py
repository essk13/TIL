def max_sum():
    case = int(input())
    number_zone = []
    max_sum = 0
    # 100*100 숫자 행렬 2중 리스트로 생성
    for n in range(100):
        numbers = list(map(int, input().split()))
        
        # 가로줄의 합중 가장 큰 값을 max_sum에 저장
        if sum(numbers) > max_sum:
            max_sum = sum(numbers)
        number_zone.append(numbers)

    # 세로줄과 좌상에서 우하로 대각선 줄의 합이 max_sum 보다 크다면 max_sum에 저장
    sum_cross = 0
    for x in range(100):
        sum_y = 0
        for y in range(100):
            sum_y += number_zone[y][x]
        if sum_y > max_sum:
            max_sum = sum_y
        
        sum_cross += number_zone[x][x]

    if sum_cross > max_sum:
        max_sum = sum_cross

    # 좌하에서 우상으로 대각선 줄의 합이 max_sum 보다 크다면 max_sum에 저장
    i = 99
    j = 0
    sum_cross = 0
    while  j < 100:
        sum_cross += number_zone[j][i]
        i -= 1
        j += 1

    if sum_cross > max_sum:
        max_sum = sum_cross

    return max_sum

case_num = 10

for case in range(case_num):
    print(f'#{case+1} {max_sum()}')