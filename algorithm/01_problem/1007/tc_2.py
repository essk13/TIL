def choice(lv):
    cnt = 0
    if lv == N:
        return 1
    for i in range(3):
        if p[lv-1] != choco[i] or p[lv-2] != choco[i]:
            p[lv] = choco[i]
            cnt += choice(lv + 1)
            p[lv] = ''
    return cnt

for tc in range(3, 15):
    choco = ['A', 'B', 'C']
    N = tc
    p = [''] * N
    ans = choice(0)
    print('#{} {}'.format(tc+1, ans))
