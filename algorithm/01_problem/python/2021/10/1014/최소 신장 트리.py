import sys
sys.stdin = open('tree.txt', 'r')

def Find(a):
    if rep[a] == a: return a
    ret = Find(rep[a])
    rep[a] = ret
    return ret


def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        rep[pb] = pa
    return


for tc in range(int(input())):
    V, E = map(int, input().split())
    path = [list(map(int, input().split())) for _ in range(E)]
    path.sort(key=lambda x:x[2])
    rep = list(range(V + 1))
    ans = 0
    for p in path:
        a = Find(p[0])
        b = Find(p[1])
        if a != b:
            Union(a, b)
            ans += p[2]
    print('#{} {}'.format(tc+1, ans))
