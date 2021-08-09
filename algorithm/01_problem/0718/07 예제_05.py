# 07 내장함수_05
# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
# 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.

# input = 
# output = [2, 4, 6, 8, 10]

def even(numbers):
    even_numbers = filter(lambda x : x % 2 == 0, numbers)
    print(list(even_numbers))

ret_even = even(range(1, 11))