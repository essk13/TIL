N = int(input())
adj = [list(map(int, input().split())) for _ in range(N**2)]
ck = [[1] * N for _ in range(N)]
room = [[0] * N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

seat = [0, 0, 0, 0]
num = 0
turn = 0
while num < N ** 2:     # for n in range(N**2):
    for r in range(N):
        for c in range(N):
            if ck[r][c]:
                turn += 1
                if turn == 1:
                    seat[0] = r
                    seat[1] = c
                st = adj[num]
                blank = 0
                love = 0
                for i in range(4):
                    y, x = r + dy[i], c + dx[i]
                    if y < 0 or y >= N or x < 0 or x >= N: continue
                    if room[y][x] == 0: blank += 1
                    if room[y][x] in st: love += 1

                if love < seat[2]: continue
                elif love == seat[2] and blank <= seat[3]: continue
                elif love == seat[2] and blank > seat[3]:
                    seat = [r, c, love, blank]
                elif love > seat[2]:
                    seat = [r, c, love, blank]

    yi, xi = seat[0], seat[1]
    room[yi][xi] = st[0]
    ck[yi][xi] = 0
    num += 1
    seat = [0, 0, 0, 0]
    turn = 0

adj.sort()
ans = 0
for r in range(N):
    for c in range(N):
        ret = 0
        for i in range(4):
            y, x = r + dy[i], c + dx[i]
            if y < 0 or y >= N or x < 0 or x >= N: continue
            if room[y][x] in adj[room[r][c]-1]: ret += 1
        ans += score[ret]

print(ans)
