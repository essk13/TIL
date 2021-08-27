T = int(input())
for tc in range(T):
    now = input()
    restore = ['1', '0']
    cnt = 0
    for i in range(len(now)):
        if now[i] == restore[cnt%2]:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))
