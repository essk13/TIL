def palindrome_length():
    '''
    가장 긴 회문의 길이를 구하는 함수
    '''
    puzzle = []
    for line in range(100):
        puzzle.append(list(input()))

    word = []
    palindrome = 0

    # 가로줄 회문 길이 확인
    for y in range(100):
        for x in range(100):
            for i in range(100):
                if x + i >= 100:
                    break
                word.append(puzzle[y][x+i])

                # 시작 문자와 같은 문자를 만나는 경우마다 회문 여부 및 최장길이 확인
                if puzzle[y][x+i] == puzzle[y][x] and word == word[::-1] and len(word) > palindrome:
                    palindrome = len(word)
            word = []


    # 세로줄 회문 길이 확인
    for x in range(100):
        for y in range(100):
            for i in range(100):
                if y + i >= 100:
                    break
                word.append(puzzle[y+i][x])

                # 시작 문자와 같은 문자를 만나는 경우마다 회문 여부 및 최장길이 확인
                if puzzle[y+i][x] == puzzle[y][x] and word == word[::-1] and len(word) > palindrome:
                    palindrome = len(word)
            word = []

    return palindrome

test_case = 10

for case in range(test_case):
    case_num = int(input())
    print(f'#{case_num} {palindrome_length()}')