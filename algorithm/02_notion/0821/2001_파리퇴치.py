import sys
sys.stdin = open('2001.txt', 'r')

def f_killer(x, y, size):
    kill = 0
    # 주어진 시작 값에서 size * size 범위의 파리의 합 계산
    for r in range(y, y+size):
        for c in range(x, x+size):
            kill += fly[r][c]

    return kill

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    # M 사이즈의 파리채 구역이 이동 가능한 범위를 이동하면서 f_killer 함수 호출
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            ret = f_killer(y, x, M)
            # 함수의 반환값이 최고값보다 크면 최고값 변경
            if ret > max_kill:
                max_kill = ret

    print('#{} {}'.format(tc+1, max_kill))