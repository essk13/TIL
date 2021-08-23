import sys
sys.stdin = open('12587.txt', 'r')

T = int(input())
for tc in range(T):
    # 중복된 문자확인을 제거하기 위해 set 함수로 입력받은 후 리스트로 변환
    str1 = set(input())
    str1 = list(str1)
    str2 = input()
    max_char = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            # str1에 있는 문자를 만나는 경우 카운트
            if str1[i] == str2[j]:
                cnt += 1
        # 가장 많이 나온 문자의 숫자보다 카운트가 크다면 최고값 변경
        if cnt > max_char:
            max_char = cnt

    print('#{} {}'.format(tc+1, max_char))