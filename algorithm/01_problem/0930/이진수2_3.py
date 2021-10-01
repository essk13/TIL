def f_bin(n, lv, total):
    global ret, d
    if lv == 13:
        ret.append(n)
        d.append(total)
        return
    f_bin(n + '1', lv + 1, total + (2**-lv))
    f_bin(n + '0', lv + 1, total)
    return


ret = []
d = []
f_bin('', 1, 0)
b = dict(zip(d, ret))

for tc in range(int(input())):
    N = float(input())
    if N in d:
        ans = str(b[N]).rstrip('0')
        print('#{} {}'.format(tc + 1, ans))
    else: print('#{} {}'.format(tc+1, 'overflow'))
