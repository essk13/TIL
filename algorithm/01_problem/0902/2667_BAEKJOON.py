def house(y, x):
    queue = [[y, x]]
    cnt = 1
    while queue:
        now = queue.pop(0)
        now_y, now_x = now[0], now[1]
        for i in range(4):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if MAP[ny][nx] == '1' and check[ny][nx] == 0:
                    cnt += 1
                    check[ny][nx] = 1
                    queue.append([ny, nx])
    return cnt


N = int(input())
MAP = [input() for _ in range(N)]
check = [[0]*N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
group = []

for y in range(N):
    for x in range(N):
        if MAP[y][x] == '1' and check[y][x] == 0:
            check[y][x] = 1
            ret = house(y, x)
            group.append(ret)

group.sort()
print(len(group))
for i in range(len(group)):
    print(group[i])
