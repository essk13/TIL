def diagonal():
    r = 0
    c = 0
    total1 = 0
    while r < 100:
        total1 += MAP[r][c]
        r += 1
        c += 1
    r = 0
    c = 99
    total2 = 0
    while r < 100:
        total2 += MAP[r][c]
        r += 1
        c -= 1
    return max(total1, total2)


def col(c):
    r = 0
    total = 0
    while r < 100:
        total += MAP[r][c]
        r += 1
    return total


def row(r):
    c = 0
    total = 0
    while c < 100:
        total += MAP[r][c]
        c += 1
    return total


T = 10
for tc in range(10):
    case = '#' + input()
    MAP = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    for x in range(100):
        ret = col(x)
        if ret > ans:
            ans = ret

    for y in range(100):
        ret = row(y)
        if ret > ans:
            ans = ret

    ret = diagonal()
    if ret > ans:
        ans = ret

    print(case, ans)
