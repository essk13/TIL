# 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

# [제약 사항]
# 1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
# 2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

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
    for a in range(0, 9, 3):
        line_numset_y = []
        line_numset_x = []
        for b in range(a, a+3):
            for c in range(3):
                line_numset_y.append(sudoku_area[b][c])
                line_numset_x.append(sudoku_area[c][b])
        if len(set(line_numset_y)) != 9 or len(set(line_numset_x)) != 9:
            return 0

    return 1

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {sudoku_check()}')