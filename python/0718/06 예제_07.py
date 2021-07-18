# 06 함수의_기초_07
# 다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
# 팩토리얼 값을 구하는 프로그램을 작성하십시오.

# input = 5
# output = 120

def number():
    num = int(input('숫자를 입력하십시오: '))
    return num

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

input_number = number()
ret_facorial = factorial(input_number)
print(ret_facorial)