# 07 내장함수_04
# ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.

# input = 65
# output = ASCII 65 => A

def ascii_code():
    code_num = int(input('ASCII 코드를 입력하십시오: '))
    return code_num

def ascii_letter(code):
    result = chr(code)
    print(f'ASCII {code} => {result}')

code_input = ascii_code()
ret_ascii = ascii_letter(code_input)
