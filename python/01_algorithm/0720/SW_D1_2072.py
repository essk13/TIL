# SW_D1_2072
# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.

# [input]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

# [output]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

num_case = int(input())

def odd_sum():
    numbers = input()
    numbers = list(numbers.split(' '))
    numbers = list(map(int, numbers))
    odd_total = 0

    for number in numbers:
        if number % 2:
            odd_total += number
        
    return odd_total

for num in range(1, num_case + 1):
    case_n = odd_sum()
    print(f'#{num} {case_n}')