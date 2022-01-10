def Find(a):
    if rep[a] == a:
        return a
    ret = Find(rep[a])
    rep[a] = ret
    return ret


def Union(a, b):
    global group
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        rep[pb] = pa
        group -= 1
    return


for tc in range(int(input())):
    N, M = map(int, input().split())
    rep = list(range(N+1))
    group = N
    for i in range(M):
        p, c = map(int, input().split())
        a = Find(p)
        b = Find(c)
        if a != b:
            Union(p, c)

    print('#{} {}'.format(tc+1, group))
