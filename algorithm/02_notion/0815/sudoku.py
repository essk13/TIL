def sudoku():
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    for y in range(9):
        line_x = set()
        line_y = set()
        for x in range(9):
            line_x.add(puzzle[y][x])
            line_y.add(puzzle[x][y])

        if len(line_x) != 9 or len(line_y) != 9:
            return 0

    x = y = 0
    while x < 7 and y < 7:
        box = set()
        for i in range(y, y + 3):
            for j in range(x, x + 3):
                box.add(puzzle[i][j])

        if len(box) != 9:
            return 0

        x += 3
        if x > 7:
            x = 0
            y += 3

    return 1

T = int(input())
for tc in range(T):
    print('#{} {}'.format(tc+1, sudoku()))