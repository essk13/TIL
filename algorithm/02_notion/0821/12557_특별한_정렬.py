import sys
sys.stdin = open('12557.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    # 10개의 숫자만 출력하면 되기 때문에 i를 0~9까지 반복
    for i in range(10):
        for j in range(i, N):
            # i가 홀수면 최소값 >> 다음 최소값 순으로 정렬
            if i % 2 and num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
            # i가 짝수면 최대값 >> 다음 최대값 순으로 정렬
            elif i % 2 == 0 and num[i] < num[j]:
                num[i], num[j] = num[j], num[i]

    print('#{}'.format(tc+1), end=' ')
    # 0 ~ 9 번 인덱스 까지 출력
    print(*num[:10])