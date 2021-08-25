T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    ans = 'ON'

    if M % 2 == 0:  # 짝수는 마지막 숫자가 0이므로 항상 OFF
        ans = 'OFF'
    else:
        M = bin(M)  # M을 2진수로 변환
        M = str(M)  # 2진수 M을 문자열로 변환
        if (len(M) - 2) < N:    # 이진수 M의 길이가 N보다 작으면 항상 OFF
            ans = 'OFF'
        else:
            for i in range(len(M)-1, len(M)-N-1, -1):   # 뒤에서 부터 N개 만큼 0인지 아닌지 비교
                if M[i] == '0':  # 0 이라면 OFF
                    ans = 'OFF'
                    break

    print(M)
    print('#{} {}'.format(tc+1, ans))
