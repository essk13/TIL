# 05 흐름과 제어_반복문 예제_09
# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

# input = 
# output = 
# *******
#  *****
#   ***
#    *

i = 7

while i >= 1:
    result = '*' * i
    print('{:^7}'.format(result))
    i -= 2