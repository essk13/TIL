import sys
sys.stdin = open('1945.txt', 'r')

# 소인수분해에 사용할 소수 사전 정의
prime_factor = [2, 3, 5, 7, 11]

T = int(input())
for tc in range(T):
    N = int(input())
    factorization = [0] * 5
    factor = 0
    # 소인수분해가 완료될 때 까지 시행 (N은 소인 수 분해 완료 시 무조건 1이 되는 정수)
    while N > 1:
        # 나머지가 0이 아니면 다음 소수로 수인수 분해 진행
        if N % prime_factor[factor] != 0:
            factor += 1
            continue
        # N을 소수로 나눈 몫으로 초기화 및 해당 소수 카운트 += 1
        N //= prime_factor[factor]
        factorization[factor] += 1

    factorization = list(map(str, factorization))
    ans = ' '.join(factorization)
    print('#{} {}'.format(tc+1, ans))