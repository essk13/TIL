N = 4
parent = [
    [(-1, -1) for _ in range(N)] for _ in range(N)
]


def Find(a):  # a 는 튜플
    if parent[a[0]][a[1]] == (a[0], a[1]):
        return (a[0], a[1])
    ret = Find(parent[a[0]][a[1]])  # a의 최종부모
    parent[a[0]][a[1]] = ret
    return ret


def Union(a, b):  # a,b 는 튜플
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        parent[pb[0]][pb[1]] = pa
    return


M = 7
cmd = [(1, 2), (0, 1), (2, 1), (1, 1), (2, 3), (3, 2), (3, 3)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(M):
    r, c = cmd[i][0], cmd[i][1]
    # r,c 에 땅 생겨라
    if Find((r, c)) == (-1, -1):  # 땅이 없다
        parent[r][c] = (r, c)  # 자기자신이 부모

    # 상하좌우로 연결하기
    for t in range(4):
        nr = r + dr[t]
        nc = c + dc[t]
        if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
        pa = Find((nr, nc))
        if pa == (-1, -1): continue
        Union((r, c), (nr, nc))

cnt = 0
for r in range(N):
    for c in range(N):
        if parent[r][c] == (r, c): cnt += 1

print(cnt)