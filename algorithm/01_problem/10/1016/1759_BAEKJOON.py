def password(lv, st):
    if lv == L:
        cnt = 0
        for i in vowel:
            if i in p: cnt += 1
        if 0 < cnt < L-1:
            print(''.join(p))
        return
    for j in range(st, M):
        if u[j]:
            u[j] = 0
            p[lv] = lst[j]
            password(lv+1, j+1)
            u[j] = 1
            p[lv] = ''
    return


L, M = map(int, input().split())
lst = input().split()
lst.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
p = [''] * L
u = [1] * M
password(0, 0)
