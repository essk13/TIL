# 05 흐름과 제어_반복문 예제_03
# 1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.

# input = 
# output = 2 4 6 8 10 12 14 16 18 ... 90 92 94 96 98 100

numbers = []

for number in range(1, 101):
    if number % 2 == 0:
        numbers.append(number)

print(' '.join(list(map(str, numbers))))