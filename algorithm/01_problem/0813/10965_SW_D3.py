def prime():
    n = set(range(2, 3164))
    for i in range(2, 3164):
        for j in range(i, 3164, i):
            if i != j:
                n.discard(j)
    return list(n)


prime_num = prime()
T = int(input())
lst_b = [0]*T

for tc in range(T):
    A = int(input())

    ans = 1
    for i in range(len(prime_num)):
        pf = prime_num[i]
        cnt = 0
        while A % pf == 0 and A >= 1:
            A //= pf
            cnt = 1 - cnt
        if cnt == 1:
            ans *= pf
        if A == 1:
            break
    if A > 1:
        ans *= A

    lst_b[tc] = '#{} {}'.format(tc+1, ans)

print('\n'.join(lst_b))