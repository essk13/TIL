    # 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# "YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def calendar():

    date_num = input()
    year = date_num[0:4]
    month = date_num[4:6]
    date = date_num[6:8]

    if int(month) > 12:
        result = -1
    elif int(month) <= 0:
        result = -1
    elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(date) > 31 or int(date) < 1:
            result = -1
        else:
            result = f'{year}/{month}/{date}'
    elif int(month) in [4, 6, 9, 11]:
        if int(date) > 30  or int(date) < 1:
            result = -1
        else:
            result = f'{year}/{month}/{date}'
    elif int(month) == 2  or int(date) < 1:
        if int(date) > 28:
            result = -1
        else:
            result = f'{year}/{month}/{date}'

    return result

case_num = int(input())

for number in range(case_num):
    print(f'#{number + 1} {calendar()}')