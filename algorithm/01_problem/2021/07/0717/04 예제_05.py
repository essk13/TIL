# 04 흐름과 제어 예제_05
# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 출력 시 아스키코드를 함께 출력합니다.

# input = c
# ouput = c(ASCII: 99) => C(ASCII: 67)

enter = input('문자를 입력하십시오: ')

if enter.isupper():
    result = enter.lower()
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(enter, ord(enter), result, ord(result)))

elif enter.islower():
    result = enter.upper()
    print('{}(ASCII: {}) => {}(ASCII: {})'.format(enter, ord(enter), result, ord(result)))

else:
    result = None
    print('{}(ASCII: {})'.format(enter, ord(enter)))