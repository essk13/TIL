import sys
from collections import deque
input = sys.stdin.readline


def diffusion(now):
    spread = [[0] * C for _ in range(R)]
    while now:
        r, c = now.popleft()
        dt = MAP[r][c]
        for i in range(4):
            y, x = r + dy[i], c + dx[i]
            if y < 0 or y >= R or x < 0 or x >= C: continue
            if MAP[y][x] == -1: continue
            spread[y][x] += (dt // 5)
            MAP[r][c] -= (dt // 5)

    for y in range(R):
        for x in range(C):
            MAP[y][x] += spread[y][x]


def high():
    # 좌상
    for r in range(cleaner[0] - 1, 0, -1):
        MAP[r][0] = MAP[r-1][0]

    # 상우
    for c in range(C - 1):
        MAP[0][c] = MAP[0][c+1]

    # 우하
    for r in range(0, cleaner[0]):
        MAP[r][C-1] = MAP[r+1][C-1]

    # 하좌
    for c in range(C-1, 1, -1):
        MAP[cleaner[0]][c] = MAP[cleaner[0]][c-1]

    MAP[cleaner[0]][1] = 0


def row():
    # 좌하
    for r in range(cleaner[1] + 1, R - 1):
        MAP[r][0] = MAP[r+1][0]

    # 하우
    for c in range(C - 1):
        MAP[R-1][c] = MAP[R-1][c + 1]

    # 우상
    for r in range(R - 1, cleaner[1], -1):
        MAP[r][C-1] = MAP[r-1][C-1]

    # 상좌
    for c in range(C - 1, 1, -1):
        MAP[cleaner[1]][c] = MAP[cleaner[1]][c - 1]

    MAP[cleaner[1]][1] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]

t = 0
cleaner = []
while t < T:
    # 미세먼지 확산
    dust = deque()
    for y in range(R):
        for x in range(C):
            if t == 0 and MAP[y][x] == -1:
                cleaner.append(y)
            elif MAP[y][x] > 0:
                dust.append((y, x))

    diffusion(dust)

    # 공기청정기 가동
    high()
    row()

    t += 1

# ans = 2
# for y in range(R):
#     ans += sum(MAP[y])
ans = 0
for y in range(R):
    for x in range(C):
        if MAP[y][x] > 0:
            ans += MAP[y][x]

print(ans)
