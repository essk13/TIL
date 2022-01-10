def palindrome_count():
    '''
    퍼즐 판의 회문의 개수를 구하는 함수
    '''
    length = int(input())
    puzzle = []

    # 퍼즐판 생성
    for i in range(8):
        puzzle.append(list(input()))

    palindrome = 0
    word = []

    # 가로줄의 회문 개수 검사
    for y in range(8):
        for x in range(8):
            for i in range(0, length):
                if x + i > 7:
                    break
                else:
                    word.append(puzzle[y][x+i])

            # 회문 길이 개수만큼 잘라 회문여부 판별
            if word == list(reversed(word)) and len(word) == length:
                palindrome += 1
            word = []

    # 세로줄의 회문 개수 검사
    for x in range(8):
        for y in range(8):
            for i in range(0, length):
                if y + i > 7:
                    break
                else:
                    word.append(puzzle[y+i][x])

            # 회문 길이 개수만큼 잘라 회문여부 판별
            if word == list(reversed(word)) and len(word) == length:
                palindrome += 1
            word = []

    return palindrome

test_case = 10

for case in range(test_case):
    print(f'#{case+1} {palindrome_count()}')