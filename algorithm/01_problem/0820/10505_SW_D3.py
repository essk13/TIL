'''
소득 불균형
'''

T = int(input())
for tc in range(T):
    N = int(input())
    income = list(map(int, input().split()))
    avg = sum(income) / N

    cnt = 0
    for i in range(N):
        if income[i] <= avg:
            cnt += 1

    print('#{} {}'.format(tc+1, cnt))