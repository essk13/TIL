# 05 흐름과 제어_반복문 예제_05
# 1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.

# input = 
# output = 1부터 100사이의 숫자 중 3의 배수의 총합: 1683

numbers = []

for number in range(1, 101):
    if number % 3 == 0:
        numbers.append(number)

sum_num = sum(numbers)

print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {sum_num}')