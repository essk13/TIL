import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
MAP = [[5] * N for _ in range(N)]
add = [list(map(int, input().split())) for _ in range(N)]
trees = []
for i in range(M):
    x, y, z = map(int, input().split())
    trees.append([x-1, y-1, z, 0])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for year in range(K):
    trees.sort(key=lambda x: x[2])
    # 봄 - 나이 +1 or 사망
    for i in range(len(trees)):
        x, y, z, d = trees[i]
        if d: continue
        if MAP[x][y] < z:
            trees[i][3] = 1
            continue
        MAP[x][y] -= z
        trees[i][2] += 1

    # 여름 - 시체 양분화
    for i in range(len(trees)):
        x, y, z, d = trees[i]
        if d == 1:
            MAP[x][y] += (z // 2)
            trees[i][3] += 1

    # 가을 - 번식
    for i in range(len(trees)):
        x, y, z, d = trees[i]
        if d: continue
        if z % 5 == 0:
            for j in range(8):
                r, c = x + dx[j], y + dy[j]
                if r < 0 or r >= N or c < 0 or c >= N: continue
                trees.append([r, c, 1, 0])

    # 겨울 - 영양 추가
    for x in range(N):
        for y in range(N):
            MAP[x][y] += add[x][y]

cnt = 0
for i in range(len(trees)):
    x, y, z, d = trees[i]
    if d == 0:
        cnt += 1

print(cnt)
