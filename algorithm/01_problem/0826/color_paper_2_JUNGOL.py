N = int(input())
paper = [[0]*102 for _ in range(102)]
color = []
cnt = 0
cross = 0
for i in range(N):
    x, y = map(int, input().split())
    st_y = y + 1
    st_x = x + 1
    ed_y = y + 10
    ed_x = x + 10
    color.append([st_y, ed_y, st_x, ed_x])

    for y in range(st_y, ed_y+1):
        for x in range(st_x, ed_x+1):
            if paper[y][x] == 0:
                paper[y][x] = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for y in range(102):
    for x in range(102):
        if paper[y][x] == 1:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < 102 and 0 <= nx < 102:
                    if paper[ny][nx] == 0:
                        cnt += 1

print(cnt)