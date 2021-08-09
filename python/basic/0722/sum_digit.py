# 입력 값의 각 자리수 숫자 합 계산함수
def sum_digit(number):
    str_number = list(str(number))
    total = sum(list(map(int, str_number)))
    return total

print(sum_digit(1234))
print(sum_digit(4567))