T = int(input())
for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    
    # 2 ~ N-1 번째 숫자들 중 좌, 우 숫자 사이 범위에 있는 숫자 개수 확인
    for i in range(1, N-1):
        if num[i-1] < num[i] < num[i+1] or num[i+1] < num[i] < num[i-1]:
           cnt += 1

    print('#{} {}'.format(tc+1, cnt))
