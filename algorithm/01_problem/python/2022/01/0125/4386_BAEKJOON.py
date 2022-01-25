import sys, math
input = sys.stdin.readline


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        rep[pb] = pa
    return


def find(a):
    if rep[a] == a: return a
    ret = find(rep[a])
    rep[a] = ret
    return ret


n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

dist = []
# 각 별들 사이의 거리 계산
for i in range(n):
    for j in range(i + 1, n):
        ix, iy = stars[i]
        jx, jy = stars[j]

        w = abs(ix - jx)
        h = abs(iy - jy)

        di = math.sqrt(w ** 2 + h ** 2)
        dist.append([di, i, j])

# 별간의 거리 순(오름차순)으로 정렬
dist.sort(key=lambda x:x[0])

ans = 0
rep = list(range(n))
for d in dist:
    '''
    1. a, b 별이 연결되었는지 확인
    2. 연결되지 않았다면 연결
    '''
    a = find(d[1])
    b = find(d[2])
    if a != b:
        union(a, b)
        ans += d[0]

print(ans)
