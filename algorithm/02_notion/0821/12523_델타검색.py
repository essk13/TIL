import sys
sys.stdin = open('12523.txt', 'r')

T = 10
for tc in range(T):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]
    # 상, 우, 하, 좌 순서로 이동하기 위한 dx, dy 생성
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    total = 0
    for y in range(N):
        for x in range(N):
            i = 0
            # 인덱스를 조절하여 상, 우, 하, 좌 순서로 값 탐색 및 계산
            while i < 4:
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:
                    num = arr[y+dy[i]][x+dx[i]]
                    total += abs(arr[y][x] - num)
                i += 1

    print('#{} {}'.format(tc+1, total))