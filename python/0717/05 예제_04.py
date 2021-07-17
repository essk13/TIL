# 05 흐름과 제어_반복문 예제_04
# 1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.

# input = 
# output = 1, 3, 5, 7, 9, ... 95, 97, 99

numbers = []

for number in range(1, 101):
    if number % 2 != 0:
        numbers.append(number)

print(', '.join(list(map(str, numbers))))