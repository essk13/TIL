# 06 함수의_기초_03
# 소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가
# 소수인지를 판단하는 프로그램을 작성하십시오.
# 소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력

# input = 13
# output = 소수입니다.

divisor = []

def number():
    num = int(input('숫자를 입력하십시오: '))
    return num

def prime_number(n):
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    
    if len(divisor) == 2:
        print('소수입니다.')
    else:
        print('소수가 아닙니다.')

number_prime = number()
ret_prime = prime_number(number_prime)
