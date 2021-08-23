import sys
sys.stdin = open('4406.txt', 'r')

vowel = ['a', 'e', 'i', 'o', 'u']

T = int(input())
for tc in range(T):
    word = input()
    n_word = ''
    for i in range(len(word)):
        for j in range(5):
            # 단어의 문자가 모음일 경우 반복문 종료
            if word[i] == vowel[j]:
                break
        # 반복문이 정상 종료될 시 새 단어에 추가
        else:
            n_word += word[i]

    print('#{} {}'.format(tc+1, n_word))