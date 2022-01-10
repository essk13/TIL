from collections import deque


def check(r, c):
    global ret
    qu = deque([[r, c, MAP[r][c]]])
    while qu:
        y, x, num = qu.popleft()
        if len(num) == 7:
            ret.add(num)
            continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4:
                qu.append([ny, nx, num + MAP[ny][nx]])
    return


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    MAP = [input().split() for _ in range(4)]
    ret = set()
    for i in range(4):
        for j in range(4):
            check(i, j)
    print('#{} {}'.format(tc+1, len(ret)))
