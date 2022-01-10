T = int(input())
for tc in range(T):
    p, q = map(float, input().split())
    s1 = float((float(1) - p) * q)
    s2 = float(p * (float(1)-q) * q)
    ans = 'NO'

    if s1 < s2:
        ans = 'YES'

    print('#{} {}'.format(tc+1, ans))
