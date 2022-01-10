import sys, time
input = sys.stdin.readline

start = time.time()
N, M, K = map(int, input().split())
add = [list(map(int, input().split())) for _ in range(N)]
MAP = [[5] * N for _ in range(N)]

trees = [[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for year in range(K):
    # 봄 - 나이 +1 or 사망
    for x in range(N):
        for y in range(N):
            if trees[x][y]:
                trees[x][y].sort()
                live_trees, dead_trees = [], 0
                for t in trees[x][y]:
                    # 여름 - 시체 양분화
                    if MAP[x][y] < t:
                        dead_trees += (t // 2)
                    else:
                        MAP[x][y] -= t
                        live_trees.append(t + 1)

                MAP[x][y] += dead_trees
                trees[x][y] = []
                trees[x][y].extend(live_trees)

    if not trees:
        print(0)
        break

    # 가을 - 번식
    for x in range(N):
        for y in range(N):
            if trees[x][y]:
                for t in trees[x][y]:
                    if t % 5 == 0:
                        for i in range(8):
                            r, c = x + dx[i], y + dy[i]
                            if r < 0 or r >= N or c < 0 or c >= N: continue
                            trees[r][c].append(1)

    # 겨울 - 영양 추가
    for x in range(N):
        for y in range(N):
            MAP[x][y] += add[x][y]

ans = 0
for x in range(N):
    for y in range(N):
        ans += len(trees[x][y])
print(ans)
end = time.time()
print(f'{end - start:.5f} sec')