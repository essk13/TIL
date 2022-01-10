def monster():
    D, L, N = map(int, input().split())
    lst_n = list(range(N))
    sum_n = sum(lst_n)

    # 공격 횟수마다 n-1 * L% 만큼 데미지 증가
    T_D = D * N + sum_n * D * L * 0.01

    return int(T_D)

T = int(input())

for tc in range(T):
    print('#{} {}'.format(tc+1, monster()))