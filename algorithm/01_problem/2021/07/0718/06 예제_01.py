# 06 함수의_기초_01
# 다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
# 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.

# input = eye
# output = 
# eye
# 입력하신 단어는 회문(Palindrome)입니다.

def input_word():
    word = input('단어를 입력하십시오: ')
    return word

def circula( str_word ):
    if list(str_word) == list(str_word)[::-1]:
        print(f'{str_word}\n입력하신 단어는 회문(Palindrome)입니다.')
    else:
        print(f'{str_word}\n입력하신 단어는 회문(Palindrome)이 아닙니다.')

ip_word = input_word()
cir_word = circula(ip_word)