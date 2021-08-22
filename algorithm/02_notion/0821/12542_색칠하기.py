import sys
sys.stdin = open('12542.txt', 'r')

def painting(r1, r2, c1, c2, color):
    # 입력값의 범위를 해당 color 로 색칠
    for y in range(r1, r2+1):
        for x in range(c1, c2+1):
            # 같은 색의 경우 겹치지 않음으로 같지 않는 경우만 색칠
            if arr[y][x] != color:
                arr[y][x] += color
    return


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # 입력값을 인자로 painting 함수 호출
        painting(r1, r2, c1, c2, color)

    purple = 0
    for y in range(10):
        for x in range(10):
            if arr[y][x] >= 3:
                purple += 1

    print('#{} {}'.format(tc+1, purple))