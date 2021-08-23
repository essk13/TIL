import sys
sys.stdin = open('1213.txt', 'r', encoding='UTF8')

T = 10
for tc in range(T):
    case = '#' + input()
    string = input()
    sentence = input()
    cnt = 0
    for i in range(len(sentence) - len(string) + 1):
        # 문장의 특정 문자부터 문자열의 길이만큼 비교하면서 다른 값이 나오면 반복 종료
        for j in range(len(string)):
            if string[j] != sentence[i + j]:
                break
        # 반복문이 이상없이 수행되었다면 카운트
        else:
             cnt += 1

    print('{} {}'.format(case, cnt))