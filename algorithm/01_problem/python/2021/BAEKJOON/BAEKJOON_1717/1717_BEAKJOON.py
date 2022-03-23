import sys

def Find(num):
    if rep[num] == num:
        return num
    ret = Find(rep[num])
    rep[num] = ret
    return ret


def Union(P, C):
    p = Find(P)
    c = Find(C)
    if p != c:
        rep[c] = p
    return


n, m = map(int, sys.stdin.readline().split())
rep = list(range(n+1))
for i in range(m):
    p, A, B = map(int, sys.stdin.readline().split())
    if p:
        a = Find(A)
        b = Find(B)
        if a == b:
            print('YES')
        else:
            print('NO')
    else:
        Union(A, B)
