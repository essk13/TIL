# 05 흐름과 제어_반복문 예제_11
# for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.

# input = 
# output = 
#     *
#    **
#   ***
#  ****
# *****

for i in range(1, 6):
    star = '*' * i
    print('{:>5}'.format(star))