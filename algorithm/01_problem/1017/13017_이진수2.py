def per(lv, n):
    global N, ps
    if lv == 12:
        N.append(n)
        ps.append(''.join(p).rstrip('0'))
        return
    for i in range(1, -1, -1):
        p[lv] = str(i)
        if i:
            per(lv+1, n + (2**-(lv + 1)))
        else:
            per(lv + 1, n)
        p[lv] = ''
    return

N = []
ps = []
p = [''] * 12
per(0, 0)
ret = dict(zip(N, ps))

for tc in range(int(input())):
    n = float(input())
    if n in N:
        ans = ret[n]
    else:
        ans = 'overflow'
    print('#{} {}'.format(tc+1, ans))
