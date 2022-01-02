# 06 함수의_기초_04
# 다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.

# input = 10
# output = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

Fibonacci = []

def Fibo_number():
    number = int(input('숫자를 입력하십시오: '))
    return number

def Fibo(num):
    for n in range(1, num + 1):
        if n <= 2:
            Fibonacci.append(1)
        elif n <= num:
            result = Fibonacci[n - 3] + Fibonacci[n - 2]
            Fibonacci.append(result)

number_input = Fibo_number()
FIbo_result = Fibo(number_input)

print(list(Fibonacci))