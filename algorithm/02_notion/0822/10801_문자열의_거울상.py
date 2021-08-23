import sys
sys.stdin = open('10801.txt', 'r')

# 각 문자의 거울상을 딕셔너리 형태로 사전 정의
origin = ['b','d','p','q']
mirror = ['d','b','q','p']
image = dict(zip(origin, mirror))

T = int(input())
for tc in range(T):
    chars = input()
    n_chars = ''
    # 거울상에서 순서도 뒤집혀야 함으로 문자열을 역순으로 탐색하며 거울상 딕셔너리로 문자 변환
    for i in range(len(chars)-1, -1, -1):
        char = chars[i]
        n_chars += image[char]

    print('#{} {}'.format(tc+1, n_chars))