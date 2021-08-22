import sys
sys.stdin = open('12525.txt', 'r')

T = 10
for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    # 비트 연산자로 부분집합 확인
    for i in range(1 << N):
        subset_sum = 0
        for j in range(N):
            # 부분집합의 항목들을 subset_sum 에 누적
            if i & (1 << j):
                subset_sum += num[j]
        # 부분집합의 합이 0이면 카운트
        if subset_sum == 0:
            cnt += 1

    print('#{} {}'.format(tc+1, cnt))