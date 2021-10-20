import sys
sys.stdin = open('01.txt', 'r')

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1] * N for _ in range(N)]
    qu = []
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == 2:
                visited[y][x] = 0
                qu.append((y, x, 0))

    ans = 0
    while qu:
        r, c, turn = qu.pop(0)
        if MAP[r][c] == 1 and visited[r][c]:
            visited[r][c] = 0
            ans += 1
        visited[r][c] = 0
        if turn >= 3: continue

        for i in range(4):
            y, x = r, c
            cnt = 0
            while 0 <= y < N and 0 <= x < N and cnt < 2:
                y += dy[i]
                x += dx[i]
                if y < 0 or y >= N or x < 0 or x >= N: break
                if MAP[y][x] == 1:
                    if cnt == 0:
                        cnt += 1
                        continue
                    if cnt == 1 and visited[y][x]:
                        qu.append((y, x, turn + 1))
                        cnt += 1
                if MAP[y][x] == 0:
                    if cnt and visited[y][x]:
                        qu.append((y, x, turn + 1))


    print('#{} {}'.format(tc+1, ans))
