# 06 함수의_기초_08
# 숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
# 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.

# input = 2, 3
# output = 
# square(2) => 4
# square(3) => 9

def input_number():
    number = input('숫자를 입력하십시오: ')
    number = number.split(', ')
    number = list(map(int, number))
    return number

def square(num):
    for i in range(len(num)):
        print('square({}) => {}'.format(num[i], num[i] ** 2))

number = input_number()
ret_square = square(number)