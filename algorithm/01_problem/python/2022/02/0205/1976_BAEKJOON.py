import sys
input = sys.stdin.readline


def find(a):
    if rep[a] == a:
        return a
    res = find(rep[a])
    return res


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        rep[pb] = pa
    return


N = int(input())
M = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x:int(x) - 1, input().split()))

rep = list(range(N))
for i in range(N):
    for j in range(i+1, N):
        if adj[i][j] == 0: continue
        if find(i) == find(j): continue
        union(i, j)

ans = find(rep[plan[0]])
for city in plan:
    if find(rep[city]) != ans:
        print('NO')
        break
else:
    print('YES')
