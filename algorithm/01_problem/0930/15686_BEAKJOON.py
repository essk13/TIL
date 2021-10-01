from itertools import combinations

def combi(ck, r):
    for i in range(len(ck)):
        if r == 1:
            yield [ck[i]]
        else:
            for next in combi(ck[i+1:], r - 1):
                yield next + [ck[i]]


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[1] * N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]

ck = []
hm = []

for y in range(N):
    for x in range(N):
        if MAP[y][x] == 2:
            ck.append((y, x))
        elif MAP[y][x] == 1:
            hm.append((y, x))

# ck_com = list(combinations(ck, M))
ck_com = list(combi(ck, M))

ans = 21e8
for com in ck_com:
    ck_road = 0
    for j in hm:
        ret = 21e8
        for i in range(M):
            road = abs(com[i][0] - j[0]) + abs(com[i][1] - j[1])
            ret = min(ret, road)
        ck_road += ret
    ans = min(ans, ck_road)

print(ans)
