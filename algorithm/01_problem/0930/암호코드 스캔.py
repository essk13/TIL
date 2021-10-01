import sys
sys.stdin = open('pw.txt', 'r')

p = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']
num = list(range(10))
enc = dict(zip(p, num))

def x_b(n):
    nn = ''
    for i in range(len(n)):
        ret = int(n[i], 16)
        ret = str(bin(ret))[2:]
        if len(ret) != 4:
            c = 4 - len(ret)
            ret = ('0' * c) + ret
        nn += ret
    return nn


def p_pw(n):
    pw = n
    pt = ''
    ck = '10'
    now, cnt = 0, 1
    for i in range(pt_s - 2, -1, -1):
        if pw[i] != ck[now]:
            pt = str(cnt // (pt_s // 7)) + pt
            now += 1
            if now > 1: now = 0
            cnt = 1
        else:
            cnt += 1
    pt = str((cnt) // (pt_s // 7)) + pt
    return pt


def check(n):
    r = 7
    m = 1
    while True:
        pw = n[-r:]
        pt = ''
        ck = '10'
        now, cnt = 0, 1
        for i in range(r-2, -1, -1):
            if pw[i] != ck[now]:
                pt = str(cnt // m) + pt
                now += 1
                if now > 1: now = 0
                cnt = 1
            else: cnt += 1
        pt = str(cnt // m) + pt
        if pt in p:
            return r
        m += 1
        r += 7


def dnc(pts):
    dnc = ''
    for i in range(0, pts*8, pts):
        ret = enc[p_pw(size[i:i + pts])]
        dnc += str(ret)
    return dnc


def ck(pw):
    check = 0
    for j in range(7):
        if j % 2:
            check += int(pw[j])
        else:
            check += (3 * int(pw[j]))

    ans = check + int(pw[7])
    if ans % 10:
        return 0
    return sum(list(map(int, list(pw))))


for tc in range(int(input().rstrip())):
    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    no = []
    ans = 0
    for line in range(N):
        arr[line] = x_b(arr[line])

    for y in range(N):
        if '1' in arr[y]:
            for x in range(len(arr[y])-1, -1, -1):
                if arr[y][x] == '1':
                    con = False
                    if no:
                        for l in range(len(no)):
                            if no[l][0] <= y <= no[l][1] and no[l][2] <= x <= no[l][3]:
                                con = True
                                break
                    if con: continue
                    pt_s = check(arr[y][:x+1])
                    size = arr[y][x-((pt_s*8)-1):x+1]
                    pw = dnc(pt_s)
                    ans += ck(pw)
                    sx = x-((pt_s*8)-1)
                    ey = y
                    while ey < N and arr[ey][x] == arr[y][x]:
                        ey += 1
                    no.append((y, ey, sx, x))


    print('#{} {}'.format(tc+1, ans))