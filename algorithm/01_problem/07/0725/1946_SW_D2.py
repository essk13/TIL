# 원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.
# 문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.
# 이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. (예 : A 5    AAAAA)
# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

# [예제]
# 압축된 문서의 내용
# A 10
# B 7
# C 5

# 압축을 풀었을 때 원본 문서의 내용
# AAAAAAAAAA
# BBBBBBBCCC
# CC

# [제약사항]
# 1. 압축된 문서의 알파벳과 숫자 쌍의 개수 N은1이상 10이하의 정수이다. (1 ≤ N ≤ 10)
# 2. 주어지는 알파벳 Ci는 A~Z의 대문자이다. (i는 줄의 번호로 1~N까지의 수)
# 3. 알파벳의 연속된 개수로 주어지는 수 Ki는 1이상 20이하의 정수이다. (1 ≤ Ki ≤ 20, i는 줄의 번호로 1~N까지의 수)
# 4. 원본 문서의 너비는 10으로 고정이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어지고 다음 줄부터 N+1줄까지 Ci와 Ki가 빈 칸을 사이에 두고 주어진다.

# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 원본 문서를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def mk_text():
    total_text = []
    number = int(input())

    for num in range(number):
        alphabet = list(input().split())
        for i in range(int(alphabet[1])):
            total_text.append(alphabet[0])

    return total_text

def print_text():
    text = mk_text()
    text_len = len(text)

    for i in range(1, text_len+1):
        if i == text_len:
            print(text[i-1], end='\n')
        elif i % 10 == 0:
            print(text[i-1], end='\n')
        else:
            print(text[i-1], end='')

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1}')
    result = print_text()