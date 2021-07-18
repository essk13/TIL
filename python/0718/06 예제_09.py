# 06 함수의_기초_09
# 인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고
# 결과를 출력하는 프로그램을 작성하십시오.

# input = one, three
# output = three

def input_word():
    word = input('두개의 문자를 입력하십시오(a, b): ')
    word = word.split(', ')
    return word

def check(str_word):
    if len(str_word[0]) > len(str_word[1]):
        print(str_word[0])
    else:
        print(str_word[1])

word = input_word()
ret_check = check(word)