def f_bin(f, lv):
    global ans
    if ans == 'overflow': return
    if lv > 12: ans = 'overflow'; return
    if f == 0: return
    if f*2 >= 1: ans += '1'
    else: ans += '0'
    if f*2 >= 1: f_bin(f*2-1, lv+1)
    else: f_bin(f*2, lv+1)
    return


for tc in range(int(input())):
    N = float(input())
    ans = ''
    f_bin(N, 1)
    print('#{} {}'.format(tc+1, ans))
