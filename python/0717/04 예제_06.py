# 04 흐름과 제어 예제_06
# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.

# input = 
# ouput = 7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196

numbers = range(1, 201)
num_7_5 = []

for number in numbers:
    if number % 7 == 0 and number % 5 != 0:
        num_7_5.append(number)
    
    # and number % 5 != 0: 미작성시 elif 사용 5의 배수 제거
    # elif number % 7 == 0 and number % 5 == 0:
    #     num_7_5.remove(number)

print(','.join(list(map(str, num_7_5))))