# 07 내장함수_09
# 다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를
# 값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는
# 프로그램을 작성하십시오.

# input = 
# output = 
# a: 0
# b: 1
# c: 2
# d: 3
# e: 4
# f: 5

alphabet_list = 'abcdef'
number_list = range(6)

dictionary = dict(zip(list(alphabet_list), number_list))

def dictionary_line(dict_1):
    for key in dict_1:
        print('{}: {}'.format(key, dict_1[key]))

ret_dict = dictionary_line(dictionary)