# 04 흐름과 제어 예제_03
# 다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.

# input = b
# ouput = b 는 소문자 입니다.

alphabet = input('알파벳을 입력하십시오: ')

if alphabet.isupper():
    print (f'{alphabet} 는 대문자 입니다.')

elif alphabet.islower():
    print(f'{alphabet} 는 소문자 입니다.')

else:
    print('알파벳이 아닙니다.')