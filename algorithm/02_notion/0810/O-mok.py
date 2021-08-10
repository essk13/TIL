puzzle = []
for i in range(19):
    line = list(map(int, input().split()))
    puzzle.append(line)
white = 0
black = 0

check = []
nope = []
c = []
for i in range(19):
    for j in range(19):
        x, y = j, i
        c = []
        cnt = 0
        if puzzle[y][x] == 1:
            cnt += 1
            c = [[x+1, y+1]]
            while x+1 < 19 and puzzle[y][x+1] == 1:
                cnt += 1
                x += 1
                c.append([x+1, y+1])
            if cnt == 5:
                black += 1
                c.append([x+1, y+1])
                check.append(c)
            cnt = 1
            c = [[x + 1, y + 1]]
            x = j
            while y+1 < 19 and puzzle[y+1][x] == 1:
                cnt += 1
                y += 1
                c.append([x+1, y+1])
            if cnt == 5:
                black += 1
                c.append([x+1, y+1])
                check.append(c)
            cnt = 1
            c = [[x + 1, y + 1]]
            y = i
            while y+1 < 19 and x+1 < 19 and puzzle[y+1][x+1] == 1:
                cnt += 1
                x += 1
                y += 1
                c.append([x+1, y+1])
            if cnt == 5:
                black += 1
                c.append([x+1, y+1])
                check.append(c)
            cnt = 1
            c = [[x + 1, y + 1]]
            x, y = j, i
            while y+1 < 19 and x-1 > -1 and puzzle[y+1][x-1] == 1:
                cnt += 1
                x -= 1
                y += 1
                c.append([x+1, y+1])
            if cnt == 5:
                black += 1
                c.append([x+1, y+1])
                check.append(c)
            cnt = 1
            c = [[x + 1, y + 1]]
            x, y = j, i

        if puzzle[y][x] == 2:
            cnt += 1
            c = [[x+1, y+1]]
            while x+1 < 19 and puzzle[y][x+1] == 2:
                cnt += 1
                x += 1
            if cnt == 5:
                white += 1
                c.append([x+1, y+1])
                check.append(c)
            cnt = 1
            c = [[x + 1, y + 1]]
            x = j
            while y+1 < 19 and puzzle[y+1][x] == 2:
                cnt += 1
                y += 1
            if cnt == 5:
                white += 1
                c.append([x+1, y+1])
                check.append(c)
            cnt = 1
            c = [[x + 1, y + 1]]
            y = i
            while y+1 < 19 and x+1 < 19 and puzzle[y+1][x+1] == 2:
                cnt += 1
                x += 1
                y += 1
                c.append([x+1, y+1])
            if cnt == 5:
                white += 1
                c.append([x+1, y+1])
                check.append(c)
            cnt = 1
            c = [[x + 1, y + 1]]
            x, y = j, i
            while y+1 < 19 and x-1 > -1 and puzzle[y+1][x-1] == 2:
                cnt += 1
                x -= 1
                y += 1
                c.append([x+1, y+1])
            if cnt == 5:
                white += 1
                c.append([x+1, y+1])
                check.append(c)
            cnt = 1




if black == 1 and white == 0:
    result = 1
    point = sorted(check[0], key=lambda x: x[0])
    print(result)
    print(point[0][1], point[0][0])
elif white == 1 and black == 0:
    result = 2
    point = sorted(check[0], key=lambda x: x[0])
    print(result)
    print(point[0][1], point[0][0])
else:
    result = 0
    print(result)