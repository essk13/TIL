import sys
sys.stdin = open('12543.txt', 'r')

A = [n for n in range(1, 13)]

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1 << 12):
        subset = []
        # 부분집합을 생성하여 인자를 리스트에 추가
        for j in range(12):
            if i & (1 << j):
                subset.append(A[j])
        # 인자의 수가 N 과 같다면 합 계산
        if len(subset) == N:
            total = 0
            for idx in range(N):
                total += subset[idx]
            # 부분집합의 합이 K 와 같다면 카운트
            if total == K:
                cnt += 1

    print('#{} {}'.format(tc+1, cnt))