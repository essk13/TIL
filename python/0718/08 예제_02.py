# 08 예외처리_02 한번 더
# 리스트 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 에서,
#  사용자로 부터 인덱스를 입력 받아 숫자로 변환하는 함수

# output1 =
# data_list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 인덱스로 사용할 숫자를 입력하세요: o
# <class 'ValueError'>, invalid literal for int() with base 10: 'o'

# outpu2 =
# data_list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 인덱스로 사용할 숫자를 입력하세요: o
# <class 'IndexError'> list index out of range
# 인덱스는 0 ~ 9까지 사용할 수 있습니다.
#[9]: 10

# data_list = list(range(1, 11))

# print(f'data_list: {data_list}')

# try:
#     num = int(input('인덱스로 사용할 숫자를 입력하세요: '))
#     print('[{}]: {}'.format(num, data_list[num])
# except IndexError as exception:
#     print(exception)
# except ValueError as exception:
#     print(exception)
# except Exception as exception:
#     print(exception)


def input_index():
    num = 0
    try:
        num = int(input('인덱스로 사용할 숫자를 입력하세요: '))
    except ValueError as excepiton:
        raise excepiton
    else:
        return num

def print_in_bounds(list, index):
    value = 0
    try:
        value = list[index]
    except IndexError as exception:
        print('{} {}'.format(type(exception), exception))
        index = len(list) - 1
        print(f'인덱스는 0 ~ {index}까지 사용할 수 있습니다.')
        value = list[index]
    finally:
        print(f'[{index}]: {value}')


data_list = list(range(1, 11))

print(f'data_list: {data_list}')

try:
    num = input_index
    print_in_bounds(data_list, num)
except ValueError as exception:
    print('{}, {}'.format(type(exception), exception))
except Exception as exception:
    print(exception)