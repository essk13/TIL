import sys
sys.stdin = open('one.txt', 'r')

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


def length(a, b):
    ax, ay = island[0][a], island[1][a]
    bx, by = island[0][b], island[1][b]
    L = (abs(ax - bx) ** 2) + (abs(ay - by) ** 2)
    return L


for tc in range(int(input())):
    N = int(input())
    island = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())

    lengths = []
    for i in range(N):
        for  j in range(N):
            if i != j:
                lengths.append((length(i, j), i, j))
    lengths.sort()

    rep = list(range(N))
    ans = 0
    for l, st, ed in lengths:
        ps = Find(st)
        pe = Find(ed)
        if ps != pe:
            Union(ps, pe)
            ans += l
    ans = round(ans * E)
    print('#{} {}'.format(tc+1, ans))



#1 10000
#2 180000
#3 1125000
#4 1953913
#5 27365366
#6 337122
#7 711268755613
#8 280157
#9 521568761
#10 34
#11 375890356686
#12 68427157
#13 21404
#14 16620885
#15 4776395492
#16 54860981981
#17 24236206202
#18 132410
#19 12876964085
#20 7016649393