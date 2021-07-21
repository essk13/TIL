# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def average():
    # 10개의 정수 평균값 출력 함수
    # 결과값 = 소수점 첫째자리에서 반올림
    numbers = list(map(int,input().split()))
    total = 0
    cnt = 0
    # 정수의 총 개수 및 총합 계산
    for number in numbers:
        total += number
        cnt += 1
    # 평균 계산 및 반올림
    if (total / cnt) % 1 >= 0.5:
        result = int(total / cnt) + 1
    else:
        result = int(total / cnt)

    return result

case_num = int(input())

for num in range(case_num):
    print(f'#{num + 1} {average()}')