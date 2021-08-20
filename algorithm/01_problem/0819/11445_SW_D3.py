'''
무한사전
'''
T = int(input())
for tc in range(T):
    P = input().rstrip()
    Q = input().rstrip()
    ans = 'N'

    # P가 Q보다 길거나 P보다 2이상 Q가 길면 무조건 'Y'
    if len(P) > len(Q) or len(P) + 1 < len(Q):
        ans = 'Y'

    else:
        for i in range(len(P)+1):

            # P의 값보다 큰 Q의 값이 있으면 'Y'
            if i < len(P) and P[i] < Q[i]:
                ans = 'Y'
                break
            # P의 길이보다 큰 Q의 문자가 'a'가 아니면 'Y'
            elif i == len(P) and Q[i] != 'a':
                ans = 'Y'

    print('#{} {}'.format(tc+1, ans))