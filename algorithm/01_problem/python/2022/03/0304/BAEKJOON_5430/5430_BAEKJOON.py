import sys
input = sys.stdin.readline


def AC():
    st, ed = 0, len(arr)
    r = False
    for o in range(len(p)):
        if p[o] == 'R':
            r = not r

        elif p[o] == 'D':
            if not r:
                st += 1
            elif r:
                ed -= 1
            if st > ed:
                return 'error'

    if not r:
        return arr[st:ed]
    else:
        res = []
        for i in range(ed - 1, st - 1, -1):
            res.append(arr[i])
        return res


for tc in range(int(input())):
    p = input().strip()
    n = int(input())
    arr = input().strip().lstrip('[').rstrip(']').split(',')
    if arr[0] != '':
        arr = list(map(int, arr))
    else:
        arr = []

    ans = AC()
    if ans != 'error':
        ans = '[' + ','.join(map(str, ans)) + ']'

    print(ans)
