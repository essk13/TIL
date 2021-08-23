import sys
sys.stdin = open('12579.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    # 입력 문장의 각 단어들의 첫글자를 대문자화 하여 리스트에 저장
    abbreviation = [word[0].upper() for word in input().split()]

    print('#{} {}'.format(tc+1, ''.join(abbreviation)))