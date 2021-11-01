import sys
sys.stdin = open('pinball.txt', 'r')

def game(y, x, w):
    ny, nx = y + dy[w], x + dx[w]
    cnt = 0
    while True:
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            cnt += 1
            w = e[w]

        elif (ny, nx) == (y, x) or MAP[ny][nx] == -1:
            return cnt

        elif MAP[ny][nx] in [1, 2, 3, 4, 5]:
            w = block[MAP[ny][nx]][w]
            cnt += 1

        elif MAP[ny][nx] in [6, 7, 8, 9, 10]:
            n = MAP[ny][nx]
            for hole in worm[n]:
                if hole != [ny, nx]:
                    ny, nx = hole[0], hole[1]
                    break


        ny += dy[w]
        nx += dx[w]


a = { 0: 2, 1: 3, 2: 1, 3: 0 }
b = { 0: 1, 1: 3, 2: 0, 3: 2 }
c = { 0: 3, 1: 2, 2: 0, 3: 1 }
d = { 0: 2, 1: 0, 2: 3, 3: 1 }
e = { 0: 2, 1: 3, 2: 0, 3: 1 }
block = { 1: a, 2: b, 3: c, 4: d, 5: e }

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    worm = [[] for _ in range(11)]
    st = []
    for y in range(N):
        for x in range(N):
            n = MAP[y][x]
            if n == 0:
                st.append([y, x])
            elif n in [6, 7, 8, 9, 10]:
                worm[n].append([y, x])

    score = 0
    for p in st:
        for i in range(4):
            score = max(score, game(p[0], p[1], i))
    print('#{} {}'.format(tc+1, score))
