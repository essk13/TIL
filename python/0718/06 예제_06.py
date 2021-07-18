# 06 함수의_기초_06
# 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,
# 이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.

# input = 
# output = 
# [2, 4, 6, 8, 10]
# 5 => False
# 10 => True

input_list = [2, 4, 6, 8, 10]

def check(check_list):
    print(check_list)
    
    if 5 in check_list:
        print('5 => {}'.format(True))
    else:
        print('5 => {}'.format(False))

    if 10 in check_list:
        print('10 => {}'.format(True))
    else:
        print('10 => {}'.format(False))

checking = check(input_list)