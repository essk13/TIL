import sys
I = sys.stdin.readline

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


V, E = map(int, I().split())
adj = [list(map(int, I().split())) for _ in range(E)]
adj.sort(key=lambda x:x[2])
rep = list(range(V + 1))

ans = 0
for i in range(E):
    a, b, c = adj[i]
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        Union(a, b)
        ans += c

print(ans)
