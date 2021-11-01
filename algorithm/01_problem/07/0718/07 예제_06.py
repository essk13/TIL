# 07 내장함수_06
# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해
# 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.

# input = 
# output = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def sqare(numbers):
    print(list(map(lambda x : x ** 2, numbers)))

number_list = sqare(range(1, 11))