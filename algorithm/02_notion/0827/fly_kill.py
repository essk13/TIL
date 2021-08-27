def f_killer(r,  c):
    kill = 0
    for i in range(r, r+M):
        for j in range(c, c+M):
            kill += zone[i][j]
    return kill


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    zone = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            ret = f_killer(y, x)
            if ret > max_kill:
                max_kill = ret

    print('#{} {}'.format(tc+1, max_kill))
