import sys
sys.stdin = open('12463.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = -21e8
    min_sum = 21e8

    for i in range(N-M+1):
        # 구간은 배열의 i ~ i+(M-1)까지
        interval = arr[i:i+M]
        num_sum = 0
        # 구간의 합 계산
        for j in range(M):
            num_sum += interval[j]
        # 구간합의 최대 최소값 여부 확인 및 변경
        if num_sum > max_sum:
            max_sum = num_sum

        if num_sum < min_sum:
            min_sum = num_sum

    ans = max_sum - min_sum
    print('#{} {}'.format(tc+1, ans))