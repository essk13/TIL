def t1(lv):
    if lv == N:
        print(*p)
        return
    for i in range(6):
        p[lv] = dice[i]
        t1(lv+1)
        p[lv] = 0
    return


def t2(lv):
    if lv == N:
        print(*p)
        return

    if p[lv-1] == 0:
        st = 0
    else:
        st = p[lv-1]-1
    for i in range(st, 6):
        p[lv] = dice[i]
        t2(lv+1)
        p[lv] = 0
    return


def t3(lv):
    if lv == N:
        print(*p)
        return
    for i in range(6):
        if u[i]:
            u[i] = 0
            p[lv] = dice[i]
            t3(lv+1)
            u[i] = 1
    return


N, M = map(int, input().split())
dice = list(range(1, 7))
u = [1] * 6
p = [0] * N
if M == 1:
    t1(0)
elif M == 2:
    t2(0)
elif M == 3:
    t3(0)
