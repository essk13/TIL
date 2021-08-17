def baldMort():
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())

    if K >= N:
        K = N-1

    max_k = 0
    for y in range(N):
        for x in range(N):
            kill = 0
            for i in range(1, K+1):
                if 0 <= x - i and 0 <= y - i:
                    kill += MAP[y-i][x-i]

            for i in range(1, K+1):
                if x + i < N and 0 <= y - i:
                    kill += MAP[y-i][x+i]

            for i in range(1, K + 1):
                if 0 <= x - i and y + i < N:
                    kill += MAP[y+i][x-i]

            for i in range(1, K + 1):
                if x + i < N and y + i < N:
                    kill += MAP[y+i][x+i]

            if kill > max_k:
                max_k = kill

    return(max_k)

T = 5
for tc in range(T):
    print('#{} {}'.format(tc+1, baldMort()))