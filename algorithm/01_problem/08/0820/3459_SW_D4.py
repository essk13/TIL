'''
승자예측
'''

T = int(input())
for tc in range(T):
    N = int(input())
    x = 1
    winner = 0
    # 승자가 변경되는 주기 각각 4의 n제곱 씩 증가
    # 1 / 4 / 4 / 16 / 16 ...

    cnt = 1
    win = 0
    while x < N:
        past_x = x

        if cnt % 2:
            # 변경 주기가 홀수 인 경우 n 값 1 증가
            win += 1
            x += 4 ** win

        else:
            x += 4 ** win

        cnt += 1
        winner += 1
        if past_x < winner < x:
            break

    # 승자 번호가 홀수인 경우 'Alice' 승
    if winner % 2:
        ans = 'Alice'
    # 짝수인 경우 'Bob' 승
    else:
        ans = 'Bob'

    print('#{} {}'.format(tc+1, ans))