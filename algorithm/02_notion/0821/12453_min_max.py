import sys
sys.stdin = open('12453.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    max_num = -21e8
    min_num = 21e8

    for i in range(N):
        # 입력된 정수들의 최고값 확인
        if num[i] > max_num:
            max_num = num[i]
        # 입력된 정수들의 최소값 확인
        if num[i] < min_num:
            min_num = num[i]
    # 최고값 - 최소값 계산
    ans = max_num - min_num
    print('#{} {}'.format(tc+1, ans))