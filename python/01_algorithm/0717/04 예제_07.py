# 04 흐름과 제어 예제_07
# 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.

# input = 
# ouput = 200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288

numbers = range(100, 301)
num_1 = []

for number in numbers:
    num_2 = number // 10
    num_3 = number // 100

    if number % 2 == 0 and num_2 % 2 == 0 and num_3 % 2 == 0:
        num_1.append(number)

print(','.join(list(map(str, num_1))))