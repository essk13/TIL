'''
세제곱 구하기
'''

def prime():
    check = ['y'] * (10**6 + 1)
    for i in range(2, (10**6 + 1)):
        for n in range(i, (10**6 + 1), i):
            if n != i:
                check[n] = 'n'

    n = [2]
    for j in range(3, (10**6 + 1), 2):
        if check[j] == 'y':
            n.append(j)

    return n

'''
N이 세제곱이 되는가를 확인하는 문제임으로 (10**18)**0.5 까지의 소수가 아니라 10**6 까지의 소수만으로 계산이 가능하다.
왜냐하면 10**6 이 넘어가는 소수를 세제곱하면 10**18을 넘어가기 때문이다.
'''

prime_lst = prime()
T = int(input())
for tc in range(T):
    N = int(input())
    ans = 1
    for i in range(len(prime_lst)):
        cnt = 0

        # N을 소인수 분해
        while N % prime_lst[i] == 0 and N >= prime_lst[i]:
            N //= prime_lst[i]
            cnt += 1

        # 인자가 3의 배수가 아니면 세제곱이 아닌 정수
        if cnt != 0 and cnt % 3 != 0:
            ans = -1
            break

        # 인자가 3의 배수라면 해당 인자 ** 인자의 개수 // 3
        if cnt != 0:
            ans *= prime_lst[i] ** (cnt // 3)


    # 소인수 분해 후 N이 1이 아니면 세제곱이 아닌 정수
    if N > 1:
        ans = -1

    print('#{} {}'.format(tc+1, ans))