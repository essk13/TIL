def pattern():
    string = input()
    result = 0

    for idx in range(1, 21):

        # 시작 문자와 같은 문자를 만나는 경우
        # 최대 문자열이 10이기 때문에 뒤에 오는 9개의 문자가 동일한지 판별
        # 동일하다면 해당 index 반환
        if string[idx] == string[0]:
            for i in range(1, 10):
                if string[idx+i] != string[i]:
                    result = 0
                    break
                result = idx

        if result != 0:
            break

    return result

test_case = int(input())

for case in range(test_case):
    print(f'#{case+1} {pattern()}')