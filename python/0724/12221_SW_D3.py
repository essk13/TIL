# 아기 석환이는 최근 구구단을 배웠다. 그래서 1 이상 9 이하의 자연수 두개를 곱셈할 수 있으나, 10 이상의 자연수를 곱셈하는 방법은 모른다.
# 두 정수 A, B가 주어진다. 아기 석환이 두 정수를 곱셈할 수 있으면 곱을 출력하고, 아니면 -1을 출력하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
# 첫 번째 줄에 두 정수 A, B가 주어진다. (1 ≤ A, B ≤ 20)

# [출력]
# 각 테스트 케이스마다 정답을 출력하라.

def baby_multiply():
    numbers_str = input().split()
    numbers = list(map(int, numbers_str))

    for i in range(2):
        if len(numbers_str[i]) == 1:
            pass
        else:
            return -1

    return numbers[0] * numbers[1]

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {baby_multiply()}')