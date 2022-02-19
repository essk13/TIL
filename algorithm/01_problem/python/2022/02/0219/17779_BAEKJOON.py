import sys
from collections import deque
input = sys.stdin.readline


def area():
    res = []
    yr = yl = y
    pr = 1
    pl = -1
    for i in range(N):
        if x < i < x + d1 + d2:
            yr += pr
            yl += pl
            res.append([yl, yr])
            if yr == y + d2:
                pr = -1
            if yl == y - d1:
                pl = 1
        elif i == x:
            res.append([y, y])
        elif i == x + d1 + d2:
            res.append([y - d1 + d2, y - d1 + d2])
        else:
            res.append([0, N])
    return res


def check():
    max_ = 0
    min_ = 21e8
    a1 = a2 = a3 = a4 = a5 = 0
    for i in range(N):
        for j in range(N):
            if x <= i <= x + d1 + d2 and height[i][0] <= j <= height[i][1]:
                a5 += city[i][j]
            elif i < x + d1 and j <= y:
                a1 += city[i][j]
            elif i <= x + d2 and y < j < N:
                a2 += city[i][j]
            elif x + d1 <= i < N and j < y - d1 + d2:
                a3 += city[i][j]
            else:
                a4 += city[i][j]

    max_ = max(a1, a2, a3, a4, a5)
    min_ = min(a1, a2, a3, a4, a5)
    return max_ - min_


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]

ans = 21e8
for x in range(N):
    for d1 in range(1, N - 1):
        for y in range(N):
            for d2 in range(1, N-2):
                if x + d1 + d2 >= N or y - d1 < 0 or y + d2 >= N:
                    continue
                height = area()
                ans = min(check(), ans)

print(ans)
