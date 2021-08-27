def row():
    for y in range(9):
        check = set(MAP[y])
        if len(check) != 9:
            return 0
    return 1


def col():
    for x in range(9):
        check = set()
        for y in range(9):
            check.add(MAP[y][x])
        if len(check) != 9:
            return 0
    return 1


def square(y, x):
    check = set()
    for r in range(y, y+3):
        for c in range(x, x+3):
            check.add(MAP[r][c])
    if len(check) != 9:
        return 0
    return 1


def sudoku():
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            ans = square(y, x)
            if not ans:
                return 0
    return 1


T = int(input())
for tc in range(T):
    MAP = [list(map(int, input().split())) for _ in range(9)]
    ret = row()
    if ret:
        ret = col()
    if ret:
        ret = sudoku()

    print('#{} {}'.format(tc+1, ret))
