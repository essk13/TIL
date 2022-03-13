import sys
from copy import deepcopy
sys.stdin = open('input.txt')


def turn(k, s):
    new = [[0] * s for _ in range(s)]
    sc = s - 1
    for line in k:
        sr = 0
        for b in line:
            new[sr][sc] = b
            sr += 1
        sc -= 1
    return new


def unlock(t1, t2, s1, s2):
    si = sj = 0
    while si > -s1:
        table = deepcopy(t1)
        i = si
        for r in range(s1):
            if i < 0 or i >= s2:
                i += 1
                continue
            j = sj
            for c in range(s1):
                if s2 > j >= 0:
                    table[r][c] += t2[i][j]
                    j += 1
                elif j < 0:
                    j += 1
            i += 1

        if check(table):
            return True

        sj -= 1
        if abs(sj) >= s1:
            si -= 1
            sj = 0
    return False


def unlock2(t1, t2, s1, s2):
    si = sj = s2 - 1
    reverse = False
    while si > -s1:
        table = deepcopy(t1)
        i = si
        for r in range(s1):
            if i < 0 or i >= s2:
                i += 1
                continue
            j = sj
            for c in range(s1):
                if s2 > j >= 0:
                    table[r][c] += t2[i][j]
                j += 1
            i += 1

        if check(table):
            return True

        sj -= 1
        if sj <= -s1:
            si -= 1
            sj = s2 - 1
    return False


def check(res):
    for li in res:
        if (max(li), min(li)) != (1, 1):
            return False
    return True


for tc in range(int(input())):
    m, n = map(int, input().split())
    key = [list(map(int, input().split())) for _ in range(m)]
    lock = [list(map(int, input().split())) for _ in range(n)]
    ans = True
    for _ in range(4):
        if unlock2(lock, key, n, m):
            break
        key = deepcopy(turn(key, m))
    else:
        ans = False
    print('#{} {}'.format(tc, ans))
