import sys
I = sys.stdin.readline

N, K = map(int, I().split())

thing = [[0,0]]
bag = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    thing.append(list(map(int, I().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+v)

print(bag[N][K])


# from itertools import combinations
#
# N, K = map(int, I().split())
# thing = [list(map(int, I().split())) for _ in range(N)]
#
# ans = 0
# for i in range(N-1, -1, -1):
#     com = list(combinations(thing, i))
#     for j in range(len(com)):
#         w = v = 0
#         for n in range(i):
#             w += com[j][n][0]
#             v += com[j][n][1]
#             if w > K: break
#         else:
#             ans = max(ans, v)
#
# print(ans)