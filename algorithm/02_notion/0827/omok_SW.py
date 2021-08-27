def omok(y, x):
    for i in range(4):
        cnt = 1
        ny = y + dy[i]
        nx = x + dx[i]
        while 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] == 'o':
            cnt += 1
            ny += dy[i]
            nx += dx[i]
            if cnt >= 5:
                return 'YES'
    return 'NO'


dy = [1, 0 ,1, 1]
dx = [0, 1, 1, -1]

T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]
    ans = 'NO'
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == 'o':
                ans = omok(y, x)
                if ans == 'YES':
                    break
        if ans == 'YES':
            break

    print('#{} {}'.format(tc+1, ans))
