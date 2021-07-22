# 주어진 숫자부터 0까지 순서대로 찍어보세요
def reverse_num():
    number = int(input())
    for num in range(number, -1, -1):
        print(num, end=' ')

input_number = reverse_num()