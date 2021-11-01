# 02 변수 예제_01
# 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

# input = 9
# output = 11106

a = int(input())
result = a + (a * 11) + (a * 111) + (a * 1111)

print(result)