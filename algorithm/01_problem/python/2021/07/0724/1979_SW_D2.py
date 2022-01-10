# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

# [예제]
# N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때
# 길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로 4번)이 된다.

# [제약 사항]
# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
# 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
def word_puzzle():
    numbers = list(map(int, input().split()))
    area_puzzle = []
    # N*N 사이즈 퍼즐판을 2중 리스트(x, y 좌표)로 생성
    for number in range(numbers[0]):
        area_1 = list(map(int, input().split()))
        area_puzzle.append(area_1)
    # 좌표값 y = i일 때 x축의 단어 작성 가능 공간을 3중 리스트로 생성
    area_x = []
    for i in range(numbers[0]):
        area_xl = []
        area_x0 = []
        area_x1 = []
        for j in range(numbers[0]+1):
            if j == numbers[0]:
                area_xl.append(area_x0)
                area_xl.append(area_x1)
            elif area_puzzle[i][j] == 0:
                area_xl.append(area_x1)
                area_x0.append(area_puzzle[i][j])
                area_x1 = []
            elif area_puzzle[i][j] == 1:
                area_xl.append(area_x0)
                area_x1.append(area_puzzle[i][j])
                area_x0 = []
        area_x.append(area_xl)
    # 좌표값 x = i일 때 y축의 단어 작성 가능 공간을 3중 리스트로 생성
    area_y = []
    for i in range(numbers[0]):
        area_yl = []
        area_y0 = []
        area_y1 = []
        for j in range(numbers[0]+1):
            if j == numbers[0]:
                area_yl.append(area_y0)
                area_yl.append(area_y1)
            elif area_puzzle[j][i] == 0:
                area_yl.append(area_y1)
                area_y0.append(area_puzzle[j][i])
                area_y1 = []
            elif area_puzzle[j][i] == 1:
                area_yl.append(area_y0)
                area_y1.append(area_puzzle[j][i])
                area_y0 = []
        area_y.append(area_yl)
    # 단어 길이 리스트 생성
    word_k = []
    for num in range(numbers[1]):
        word_k.append(1)

    cnt_k = 0
    # 단어가 들어갈 수 있는 공간 개수 확인
    for x in range(numbers[0]):
        for idx_x in range(len(area_x[x])):
            if word_k == area_x[x][idx_x]:
                cnt_k += 1

    for y in range(numbers[0]):
        for idx_y in range(len(area_y[y])):
            if word_k == area_y[y][idx_y]:
                cnt_k += 1

    return cnt_k

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {word_puzzle()}')