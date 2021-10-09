import sys
sys.stdin = open('food.txt', 'r')
from itertools import combinations


for tc in range(int(input())):
    N = int(input())
    recipe = [list(map(int, input().split())) for _ in range(N)]
    u = range(N)
    com = list(combinations(u, N//2))

    min_ = 21e8
    for i in com:
        f1 = 0
        for x in i:
            for y in i:
                f1 += recipe[x][y]

        f2 = 0
        for x in range(N):
            if x not in i:
                for y in range(N):
                    if y not in i:
                        f2 += recipe[x][y]

        min_ = min(abs(f1-f2), min_)

    print('#{} {}'.format(tc+1, min_))
