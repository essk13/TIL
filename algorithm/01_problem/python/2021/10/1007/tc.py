def choice(lv):
    cnt = 0
    if (p[lv - 1] == 'B' and p[lv - 2] == 'T') or (p[lv - 1] == 'T' and p[lv - 2] == 'B'):
        return 0

    if lv == 4:
        return 1

    for i in range(4):
        p[lv] = lst[i]
        cnt += choice(lv+1)
        p[lv] = ''
    return cnt


lst = ['B', 'O', 'T', 'K']
p = [''] * 4
cnt = choice(0)
print(cnt)
