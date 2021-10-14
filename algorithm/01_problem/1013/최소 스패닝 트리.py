def Find(a):
    if MST[a] == a:
        return a
    ret = Find(MST[a])
    MST[a] = ret
    return ret


def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        MST[pb] = pa
    return


for tc in range(int(input())):
    V, E = map(int, input().split())
    MST = list(range(100001))
    total = 0
    values = [list(map(int, input().split())) for _ in range(E)]
    values.sort(key=lambda x:x[2])
    for v in values:
        a, b, c = v
        pa = Find(a)
        pb = Find(b)
        if pa != pb:
            total += c
            Union(a, b)
    print('#{} {}'.format(tc+1, total))
