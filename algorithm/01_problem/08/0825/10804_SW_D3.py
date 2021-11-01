# 문자열을 거울상으로 변경하기 위한 딕셔너리 정의
origin = ['b', 'd', 'p', 'q']
mirror = ['d', 'b', 'q', 'p']
image = dict(zip(origin, mirror))

T = int(input())
for tc in range(T):
    string = list(input())

    for i in range(len(string)):        # 문자를 거울상으로 변환
        st = string[i]
        string[i] = image[st]

    ans = ''.join(string[::-1])

    print('#{} {}'.format(tc+1, ans))
