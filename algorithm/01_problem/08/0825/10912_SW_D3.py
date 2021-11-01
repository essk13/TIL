T = int(input())
for tc in range(T):
    string = input()
    size = len(string)
    check = [1] * size      # 짝을 맞추고 난 뒤 남은 문자 확인을 위한 배열 생성

    for i in range(size):
        if check[i] == 1:   # 남은 문자인 경우 아래 반복문 수행
            for j in range(size):
                
                # 현재 문자와 비교 문자의 위치가 같지 않으면서 남은 문자이고
                # 현재 문자와 비교 문자가 같은 경우 두 문자 남은 문자에서 제거
                if i != j and check[j] == 1 and \
                    string[i] == string[j]:
                    check[i], check[j] = 0, 0
                    break

    ans = []
    for cnt in range(size):
        if check[cnt] == 1:
            ans.append(string[cnt])
    if ans:
        ans.sort()
    else:
        ans = ['Good']

    print('#{} {}'.format(tc+1, ''.join(ans)))
