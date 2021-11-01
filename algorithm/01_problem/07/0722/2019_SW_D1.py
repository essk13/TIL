# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.

def multiply_int():
    number = int(input())
    ret_milti = [1]
    result = 1
    for num in range(1, number+1):
        result *= 2
        ret_milti.append(result)
    print(*ret_milti)

input_number = multiply_int()
