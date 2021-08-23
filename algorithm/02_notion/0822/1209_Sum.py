import sys
sys.stdin = open('1209.txt', 'r')

def row(y):
    total = 0
    # 가로 y 에 대한 합 반환
    for x in range(100):
        total += arr[y][x]
    return total

def column(x):
    total = 0
    # 세로 x 에 대한 합 반환
    for y in range(100):
        total += arr[y][x]
    return total

def diagonal():
    # 우상, 우하 대각선의 합 중 더 큰값 반환
    total = 0
    x = 0
    y = 0
    while x < 100:
        total += arr[y][x]
        y += 1
        x += 1

    total2 = 0
    r = 0
    c = 99
    while r < 100:
        total2 += arr[r][c]
        r += 1
        c -= 1

    if total > total2:
        return total
    return total2


T = 10
for tc in range(T):
    case = '#' + input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    for i in range(100):
        ret = row(i)
        # 최대값과 i번 가로줄의 합 비교
        if ret > max_sum:
            max_sum = ret
        ret = column(i)
        # 최대값과 I번 세로줄의 합 비교
        if ret > max_sum:
            max_sum = ret

    ret = diagonal()
    # 최대값과 대각선 합 중 큰 값과 비교
    if ret > max_sum:
        max_sum = ret

    print('{} {}'.format(case, max_sum))