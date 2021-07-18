# 07 내장함수_07
# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
# 짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는
# 프로그램을 작성하십시오.

# input = 
# output = [4, 16, 36, 64, 100]

def even_sqare(numbers):
    even_numbers = filter(lambda x : x % 2 == 0, numbers)
    print(list(map(lambda n : n ** 2, even_numbers)))

list_number = even_sqare(range(1, 11))