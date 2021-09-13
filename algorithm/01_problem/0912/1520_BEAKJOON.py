import sys
sys.setrecursionlimit(10000)

def dfs(ny, nx):
    cnt = 0
    if ny == M - 1 and nx == N - 1:
        return 1
    for i in range(4):
        ty, tx = ny + dy[i], nx + dx[i]
        if 0 <= ty < M and 0 <= tx < N:
            if MAP[ty][tx] < MAP[ny][nx]:
                cnt += dfs(ty, tx)
    return cnt


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

M, N = map(int, input().split())
MAP = [list(map( int, input().split())) for _ in range(M)]
# visited = [[0] * N for _ in range(M)]
ans = dfs(0, 0)

print(ans)
