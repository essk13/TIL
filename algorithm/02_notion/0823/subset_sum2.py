def subset_sum(n, k, i):
    '''
    부분집합의 인자수가 n이면서 부분집합의 합이 k인
    부분집합의 수를 반환하는 함수 
    '''
    cnt = 0
    subset[n] = i
    # 부분집합의 인자 숫자가 N이고 부분집합의 합이 K인 경우 1 반환
    if n == (N - 1) and sum(subset) == k:
        subset[n] = 0
        return 1
    # 부분집합의 합이 K와 다른 경우 0 반환
    elif n == (N-1) and sum(subset) != k:
        subset[n] = 0
        return 0
    # 반복문을 수행하며 i~20까지의 i값으로 subset_sum 함수 재귀호출
    for j in range(i+1, 21):
        if used[j] == 0 and j <= k:
            # 반복 적용을 방지하기 위한 used 배열 사용
            used[j] = 1
            cnt += subset_sum(n+1, k, j)
            # 사용여부 초기화
            used[j] = 0
    return cnt


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    # 사용 여부를 확인하기 위한 배열
    used = [0] * 21
    ans = 0

    for i in range(1, 21 - N + 1):
        # 부분집합의 숫자 범위 제한
        subset = [0] * N
        ans += subset_sum(0, K, i)

    print('#{} {}'.format(tc+1, ans))
