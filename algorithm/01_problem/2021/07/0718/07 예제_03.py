# 07 내장함수_03 한번 더
# 가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
# 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.

# input = 
# output = 에러발생

def multiply(*numbers):
    result = 1
    for num in numbers:
        if type(num) != int:
            print('에러발생')
            # return 미사용시 에러 발생 이전의 결과값 출력
            return
        else:
            result *= num

    print(result)

multi = multiply(1, 2, '4', 3)