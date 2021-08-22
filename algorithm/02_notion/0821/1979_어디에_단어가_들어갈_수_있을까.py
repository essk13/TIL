import sys
sys.stdin = open('1979.txt', 'r')

def row(N, K):
    row = 0
    for y in range(N):
        x = 0
        cnt = 0
        while x < N:
            # 우측으로 이동하면서 1 인 경우 카운트
            if puzzle[y][x] == 1:
                cnt += 1
                # 1이면서 x가 마지막 값이고 카운트가 K인 경우 가능한 값 +1
                if x == (N - 1) and cnt == K:
                    row += 1
            # 0 이면서 카운트가 K이면 가능한 값 +1
            # 카운트 0으로 초기화
            elif puzzle[y][x] == 0 and cnt == K:
                row += 1
                cnt = 0
            # 그 외 경우 카운트 0으로 초기화
            else:
                cnt = 0
            x += 1
    return row


def column(N, K):
    column = 0
    for x in range(N):
        y = 0
        cnt = 0
        while y < N:
            # 아래로 이동하면서 1이면 카운트
            if puzzle[y][x] == 1:
                cnt += 1
                # 1이면서 y가 마지막 값이고 카운트가 K이면 가능한 값 +1
                if y == (N - 1) and cnt == K:
                    column += 1
            # 0이면서 카운트가 K이면 가능한 값 +1
            # 카운트 0으로 초기화
            elif puzzle[y][x] == 0 and cnt == K:
                column += 1
                cnt = 0
            # 그 외 카운트 0으로 초기화
            else:
                cnt = 0
            y += 1
    return column


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    r_cnt = row(N, K)
    c_cnt = column(N,K)

    ans = r_cnt + c_cnt
    print('#{} {}'.format(tc+1, ans))