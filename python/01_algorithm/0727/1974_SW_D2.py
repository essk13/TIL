def sudoku_check():
    # 스도쿠 판 2중 리스트로 생성
    sudoku_area = []
    for number in range(9):
        sudoku_number = list(map(int, input().split()))
        sudoku_area.append(sudoku_number)
    # 가로줄, 세로줄 겹치는 숫자 확인
    for y in range(9):
        line_numset_y = []
        line_numset_x = []
        for x in range(9):
            line_numset_y.append(sudoku_area[y][x])
            line_numset_x.append(sudoku_area[x][y])
        if len(set(line_numset_y)) != 9 or len(set(line_numset_x)) != 9:
            return 0
    # 3*3 칸 9개의 겹치는 숫자 확인
    for d in range(0, 9, 3):
        for a in range(0, 9, 3):
            line_numset_y = []
            line_numset_x = []
            for b in range(a, a+3):
                for c in range(d, d+3):
                    line_numset_y.append(sudoku_area[b][c])
                    line_numset_x.append(sudoku_area[c][b])
            if len(set(line_numset_y)) != 9 or len(set(line_numset_x)) != 9:
                return 0

    return 1

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {sudoku_check()}')