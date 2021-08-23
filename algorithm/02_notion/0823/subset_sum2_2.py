def subset_sum(i, n, total, rs):
    cnt = 0
    # 부분집합의 인자 수가 N이고 부분집합의 합이 K인 경우 1 반환
    if n == N and total == K:
        return 1
    # K가 합보다 작거나 현재 부분집합의 합 + 부분집합의 인자가 아닌 숫자들의 합이 K보다 작으면 0 반환
    elif total > K or (total + rs) < K:
        return 0
    # i가 19일때 까지 재귀호출(19+1 = 20 이므로 1~20까지의 숫자를 모두 확인)
    if i < 20:
        # i를 포함한 부분집합
        cnt += subset_sum(i + 1, n + 1, total + i + 1, rs - i - 1)
        # i를 포함하지 않은 부분집합
        cnt += subset_sum(i + 1, n, total, rs - i)
    return cnt

# 집합 A의 모든 인자의 합
rs = 210

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    cnt = subset_sum(0, 0, 0, rs)
    print('#{} {}'.format(tc + 1, cnt))
