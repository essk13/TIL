import sys
from collections import deque
input = sys.stdin.readline


def heating(r, c, p):
    temp = [[0] * C for _ in range(R)]
    q = deque([(r, c)])
    room[r][c] += 5
    t = 4
    while t > 0:
        for n in range(len(q)):
            x, y = q.popleft()
            for i in range(3):
                dx, dy = heat[p][i][0], heat[p][i][1]
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
                if temp[nx][ny]: continue

                if i == 0:
                    if p == 1:
                        if 'top' in wall[x][y] or 'left' in wall[nx][ny]: continue
                    elif p == 2:
                        if 'top' in wall[x][y] or 'right' in wall[nx][ny]: continue
                    elif p == 3:
                        if 'left' in wall[x][y] or 'bottom' in wall[nx][ny]: continue
                    elif p == 4:
                        if 'left' in wall[x][y] or 'top' in wall[nx][ny]: continue
                    q.append((nx, ny))
                    temp[nx][ny] += 1
                    room[nx][ny] += t

                elif i == 1:
                    if p == 1 and 'right' in wall[x][y]: continue
                    elif p == 2 and 'left' in wall[x][y]: continue
                    elif p == 3 and 'top' in wall[x][y]: continue
                    elif p == 4 and 'bottom' in wall[x][y]: continue
                    q.append((nx, ny))
                    temp[nx][ny] += 1
                    room[nx][ny] += t

                else:
                    if p == 1:
                        if 'bottom' in wall[x][y] or 'left' in wall[nx][ny]: continue
                    elif p == 2:
                        if 'bottom' in wall[x][y] or 'right' in wall[nx][ny]: continue
                    elif p == 3:
                        if 'right' in wall[x][y] or 'bottom' in wall[nx][ny]: continue
                    elif p == 4:
                        if 'right' in wall[x][y] or 'top' in wall[nx][ny]: continue
                    q.append((nx, ny))
                    temp[nx][ny] += 1
                    room[nx][ny] += t
        t -= 1
    return


def spread():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    ck = ['top', 'right', 'bottom', 'left']
    temp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c]:
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                    if room[r][c] < room[nr][nc]: continue
                    if ck[i] in wall[r][c]: continue

                    res = (room[r][c] - room[nr][nc]) // 4
                    temp[r][c] -= res
                    temp[nr][nc] += res

    for r in range(R):
        for c in range(C):
            room[r][c] += temp[r][c]
    return


heat = {
    1: [(-1, 1), (0, 1), (1, 1)],
    2: [(-1, -1), (0, -1), (1, -1)],
    3: [(-1, -1), (-1, 0), (-1, 1)],
    4: [(1, -1), (1, 0), (1, 1)]
}

R, C, K = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

heater = []
target = []
for r in range(R):
    for c in range(C):
        if room[r][c] not in [0, 5]:
            heater.append((r, c, room[r][c]))
        elif room[r][c] == 5:
            target.append((r, c))

room = [[0] * C for _ in range(R)]

# 벽 상태 저장
wall = [[[] for _ in range(C)] for _ in range(R)]
W = int(input())
for i in range(W):
    r, c, p = map(int, input().split())
    if p:
        wall[r-1][c-1].append('right')
        wall[r-1][c].append('left')
    else:
        wall[r-2][c-1].append('bottom')
        wall[r-1][c-1].append('top')

choco = 0
while True:
    # 온풍기 가동
    for r, c, p in heater:
        if p == 1:      # 오른쪽
            heating(r, c + 1, p)
        elif p == 2:    # 왼쪽
            heating(r, c - 1, p)
        elif p == 3:    # 위쪽
            heating(r - 1, c, p)
        else:           # 아래쪽
            heating(r + 1, c, p)

    # 온도 조절
    spread()

    # 가장자리 온도 감소
    for r in range(R):
        for c in range(C):
            if r == 0 or c == 0 or r == R - 1 or c == C - 1:
                if room[r][c]:
                    room[r][c] -= 1

    # 초콜릿 먹기
    choco += 1
    if choco > 100:
        choco = 101
        break

    # 목표 온도 달성여부 점검
    stop = True
    for tr, tc in target:
        if room[tr][tc] < K:
            stop = False
            break

    if stop:
        break

print(choco)
