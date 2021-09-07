# fail
def block(t, r, c):
    if t == 2:
        x = 1
        while x + 1 < 6 and green[x+1][c] == 0 and green[x+1][c+1] == 0:
            x += 1
        green[x][c], green[x][c+1] = 1, 1
        x = 1
        while x + 2 < 6 and blue[x+1][r] == 0 and blue[x+2][r] == 0:
            x += 1
        blue[x][r], blue[x+1][r] = 1, 1
    elif t == 3:
        x = 1
        while x + 2 < 6 and green[x+1][c] == 0 and green[x+2][c] == 0:
            x += 1
        green[x][c], green[x+1][c] = 1, 1
        x = 1
        while x + 1 < 6 and blue[x+1][r] == 0 and blue[x+1][r+1] == 0:
            x += 1
        blue[x][r], blue[x][r+1] = 1, 1
    else:
        x = 1
        while x + 1 < 6 and green[x+1][c] == 0:
            x += 1
        green[x][c] = 1
        x = 1
        while x + 1 < 6 and blue[x+1][r] == 0:
            x += 1
        blue[x][r] = 1


def check(board):
    cnt = 0
    ck = []
    for i in range(2, 6):
        if sum(board[i]) == 4:
            ck.append(i)
            cnt += 1
    for j in range(cnt):
        board.pop(ck[j])
        board.insert(0, [0]*4)

    return cnt


def delete(board):
    y = 0
    for r in range(2):
        for c in range(4):
            if board[r][c] == 1 and r == 0:
                y += 1
                break
            elif board[r][c] == 1 and r == 1:
                y += 2
                break

    if y == 1:
        for i in range(2):
            board.pop()
            board.insert(0, [0]*4)
    elif y == 2:
        board.pop()
        board.insert(0, [0]*4)


N = int(input())
blue = [[0]*4 for _ in range(6)]
green = [[0]*4 for _ in range(6)]
score = 0
for i in range(N):
    t, x, y = map(int, input().split())
    block(t, x, y)
    score += check(blue)
    score += check(green)
    delete(blue)
    delete(green)

total = 0
for j in range(6):
    total += sum(blue[j])
    total += sum(green[j])

print(score)
print(total)
