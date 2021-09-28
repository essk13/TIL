from collections import deque

def checking(r, c):
    qu = deque([(r, c)])
    ret = 0
    while qu:
        y, x = qu.popleft()
        if PC[y][x] == 2:
            ret = 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if PC[ny][nx] != 0 and check[ny][nx]:
                    check[ny][nx] = 0
                    qu.append((ny, nx))
    return ret


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N, M = map(int, input().split())
    PC = [list(map(int, input().split())) for _ in range(N)]
    check = [[1]*M for _ in range(N)]

    cnt = 0
    for y in range(N):
        for x in range(M):
            if PC[y][x] != 0 and check[y][x]:
                check[y][x] = 0
                cnt += checking(y, x)

    print('#{} {}'.format(tc+1, cnt))
