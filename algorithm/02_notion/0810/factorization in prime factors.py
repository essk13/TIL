def factorization():
    N = int(input())
    prime = [11, 7, 5, 3, 2]
    factors = [0]*5

    for i in range(5):
        cnt = 0
        while True:
            if N % prime[i] != 0:
                break
            N = N // prime[i]
            cnt += 1
        factors[i] = cnt

    factors.reverse()
    factors = list(map(str, factors))

    return ' '.join(factors)

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, factorization()))