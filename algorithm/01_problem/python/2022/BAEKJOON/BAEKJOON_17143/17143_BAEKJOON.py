import sys
from collections import defaultdict
input = sys.stdin.readline


def shark_move():
    for sh in range(M):
        if not sharks[sh]["l"]:
            continue
        m = sharks[sh]["s"]
        nd = sharks[sh]["d"]
        if nd in (1, 2):
            nr = sharks[sh]["r"]
            if nd == 1:
                if m < nr:
                    sharks[sh]["r"] = nr - m
                else:
                    m -= nr
                    m %= (R * 2) - 2
                    if m > R - 1:
                        m -= (R - 1)
                        sharks[sh]["r"] = R - 1 - m
                    else:
                        sharks[sh]["r"] = m
                        sharks[sh]["d"] = 2
            else:
                if m < (R - 1) - nr:
                    sharks[sh]["r"] = nr + m
                else:
                    m -= ((R - 1) - nr)
                    m %= (R * 2) - 2
                    if m > R - 1:
                        m -= (R - 1)
                        sharks[sh]["r"] = m
                    else:
                        sharks[sh]["r"] = R - 1 - m
                        sharks[sh]["d"] = 1
        else:
            nc = sharks[sh]["c"]
            if nd == 3:
                if m < (C - 1) - nc:
                    sharks[sh]["c"] = nc + m
                else:
                    m -= ((C - 1) - nc)
                    m %= (C * 2) - 2
                    if m > C - 1:
                        m -= (C - 1)
                        sharks[sh]["c"] = m
                    else:
                        sharks[sh]["c"] = C - 1 - m
                        sharks[sh]["d"] = 4
            else:
                if m < nc:
                    sharks[sh]["c"] = nc - m
                else:
                    m -= nc
                    m %= (C * 2) - 2
                    if m > C - 1:
                        m -= (C - 1)
                        sharks[sh]["c"] = C - 1 - m
                    else:
                        sharks[sh]["c"] = m
                        sharks[sh]["d"] = 3

        cc, cr = sharks[sh]["r"], sharks[sh]["c"]
        if MAP[cc][cr] >= 0:
            if sharks[MAP[cc][cr]]["z"] < sharks[sh]["z"]:
                sharks[MAP[cc][cr]]["l"] = 0
                MAP[cc][cr] = sh
            else:
                sharks[sh]["l"] = 0
        else:
            MAP[cc][cr] = sh
    return


def fishing():
    for x in range(R):
        if MAP[x][f] >= 0:
            sharks[MAP[x][f]]["l"] = 0
            return sharks[MAP[x][f]]["z"]
    return 0


R, C, M = map(int, input().split())
sharks = [defaultdict() for _ in range(M)]
MAP = [[-1] * C for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    MAP[r-1][c-1] = i
    sharks[i]["l"] = 1
    sharks[i]["d"] = d
    sharks[i]["r"] = r - 1
    sharks[i]["c"] = c - 1
    sharks[i]["s"] = s
    sharks[i]["z"] = z

ans = 0
for f in range(C):
    ans += fishing()
    MAP = [[-1] * C for _ in range(R)]
    shark_move()

print(ans)
