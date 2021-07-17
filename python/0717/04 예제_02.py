# 04 흐름과 제어 예제_02
# 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
# (단, 약수가 2개일 경우 소수임을 나타내십시오)

# input = 5
# ouput = 
# 1(은)는 5의 약수입니다.
# 5(은)는 5의 약수입니다.
# 5(은)는 1과 5로만 나눌 수 있는 소수입니다.

number = int(input('숫자를 입력하십시오: '))
divisor = []

for num in range(1, number +1 ):
    if number % num == 0:
        divisor.append(num)
        print(f'{num}(은)는 {number}의 약수입니다.')

if len(divisor) == 2:
    print('{}(은)는 {}과 {}로만 나눌 수 있는 소수입니다.'.format(number, divisor[0], divisor[1]))