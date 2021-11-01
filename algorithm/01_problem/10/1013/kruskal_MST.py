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


lst = [
    [0, 1, 32],
    [0, 2, 31],
    [0, 5, 60],
    [0, 6, 51],
    [1, 2, 21],
    [2, 4, 46],
    [2, 6, 25],
    [3, 4, 34],
    [3, 5, 18],
    [4, 6, 51],
    [5, 4, 40],
]

MST = list(range(7))
lst.sort(key=lambda x:x[2])
total = 0
for adj in lst:
    a, b, cost = adj
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        Union(a, b)
        total += cost

print(MST)
print(total)
