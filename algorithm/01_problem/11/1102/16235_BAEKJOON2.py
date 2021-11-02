import sys, time
from collections import deque
input = sys.stdin.readline

start = time.time()
N, M, K = map(int, input().split())
add = [list(map(int, input().split())) for _ in range(N)]
MAP = [[5] * N for _ in range(N)]

trees = deque()
for i in range(M):
    x, y, z = map(int, input().split())
    trees.append((x-1, y-1, z))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

k = 0
while k < K and trees:
    k += 1
    # 봄 - 나이 +1 or 사망
    dead_trees = deque()
    for i in range(len(trees)):
        x, y, z = trees.popleft()
        if MAP[x][y] < z:
            dead_trees.append((x, y, z // 2))
        else:
            MAP[x][y] -= z
            z += 1
            trees.append((x, y, z))

    # 여름 - 시체 양분화
    while dead_trees:
        x, y, z = dead_trees.popleft()
        MAP[x][y] += z

    # 가을 - 번식
    new_trees = deque(trees)
    for x, y, z in new_trees:
        if z % 5 == 0:
            for j in range(8):
                r, c = x + dx[j], y + dy[j]
                if r < 0 or r >= N or c < 0 or c >= N: continue
                trees.appendleft((r, c, 1))

    # 겨울 - 영양 추가
    for x in range(N):
        for y in range(N):
            MAP[x][y] += add[x][y]

print(len(trees))
end = time.time()
print(f'{end - start:.5f} sec')
