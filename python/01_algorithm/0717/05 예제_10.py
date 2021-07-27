# 05 흐름과 제어_반복문 예제_10
# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

# input = 11
# output = 
# 0 1 2 3 4 5 6 7 8 9
# 0 2 0 0 0 0 0 0 0 0

number = input('숫자를 입력하십시오: ')
numbers = range(0, 10)
cnt_number = []

for num in numbers:
    str_num = str(num)
    cnt = list(number).count(str_num)
    cnt_number.append(str(cnt))

print(' '.join(list(map(str, numbers))))
print(' '.join(cnt_number))