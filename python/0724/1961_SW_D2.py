# N x N 행렬이 주어질 때,
# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

# [제약 사항]
# N은 3 이상 7 이하이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
# 다음 N 줄에는 N x N 행렬이 주어진다.

# [출력]
# 출력의 첫 줄은 '#t'로 시작하고,
# 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 제공되는 행렬을 2중 리스트로 생성하는 함수
def first_matrix():
    number = int(input())
    matrix = []
    for num in range(number):
        matrix_line = list(input().split())
        matrix.append(matrix_line)
    
    return matrix
# 제공 받은 행렬을 90도 회전시키는 함수
def matrix_rotation(matrix):
    matrix_new = []
    number = len(matrix)
    # y축(세로) line 값을 역순으로 x축(가로) line에 대입
    for x in range(number):
        matrix_newline = []
        for y in range(number-1, -1, -1):
            matrix_newline.append(matrix[y][x])
        matrix_new.append(matrix_newline)

    return matrix_new
# 각각 90도, 180도, 270도 회전시킨 행렬을 1번 x축 ~ 마지막 x축 순으로 출력
def print_matrix():
    first = first_matrix()
    second = matrix_rotation(first)
    third = matrix_rotation(second)
    fourth = matrix_rotation(third)
    for i in range(len(first)):
        # 90도 회전 y=i 일 때 x축 출력
        print(''.join(second[i]), end=' ')
        # 180도 회전 y=i 일 때 x축 출력
        print(''.join(third[i]), end=' ')
        # 270도 회전 y=i 일 때 x축 출력
        print(''.join(fourth[i]), end='\n')

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1}')
    matrix = print_matrix()