import sys
sys.stdin = open('1954.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    # 시작값은 항상 1이므로 사전에 1 저장
    snail[0][0] = 1
    # 방향 회전을 위한 dx, dy 생성
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    i = 0
    x = 0
    y = 0
    # 입력할 숫자는 2 ~ N * N
    num = 2

    while num <= N * N:
        # 진행 방향이 배열범위를 벗어나지 않으면서 다음 항목이 0인 경우 다음 항목에 숫자 저장
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and snail[y+dy[i]][x+dx[i]] == 0:
            x += dx[i]
            y += dy[i]
            snail[y][x] = num
            # 다음 숫자로 변경 (+=1)
            num += 1
        # 위 조건을 벗어난 경우 진행방향 변경을 위해 i값 수정
        else:
            i += 1
            # i의 범위는 0 ~ 3 이므로 3을 넘어서면 0으로 초기화
            if i > 3:
                i = 0

    print('#{}'.format(tc+1))
    for j in range(N):
        print(*snail[j])