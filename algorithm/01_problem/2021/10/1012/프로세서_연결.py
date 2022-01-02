import sys
sys.stdin = open('core.txt', 'r')


def link(lv, core, line):
    global max_c, min_l
    if lv == pn:
        if core > max_c:
            max_c = core
            min_l = line
        elif core == max_c:
            min_l = min(line, min_l)
        return

    y, x = P[lv][0], P[lv][1]
    block = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        cnt = 0
        while 0 <= ny < N and 0 <= nx < N:
            if cell[ny][nx]:
                block += 1
                if i == 0 or i == 2:
                    ny -= dy[i]
                    while ny != y:
                        cell[ny][nx] = 0
                        ny -= dy[i]
                else:
                    nx -= dx[i]
                    while nx != x:
                        cell[ny][nx] = 0
                        nx -= dx[i]
                break
            cell[ny][nx] = 1
            cnt += 1
            ny += dy[i]
            nx += dx[i]

        else:
            link(lv+1, core+1, line+cnt)
            if i == 0 or i == 2:
                ny -= dy[i]
                while ny != y:
                    cell[ny][nx] = 0
                    ny -= dy[i]
            else:
                nx -= dx[i]
                while nx != x:
                    cell[ny][nx] = 0
                    nx -= dx[i]
    if block == 4:
        link(lv+1, core, line)
    return


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    cell = [list(map(int, input().split())) for _ in range(N)]

    P = []
    for y in range(1, N-1):
        for x in range(1, N-1):
            if cell[y][x] == 1:
                P.append([y, x])

    max_c = 0
    min_l = 0
    pn = len(P)
    link(0, 0, 0)
    print('#{} {}'.format(tc+1, min_l))
