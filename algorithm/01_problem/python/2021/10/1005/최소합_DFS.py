def dfs(r, c, total):
    global ans
    if (r, c) == (N-1, N-1):
        ans = min(ans, total)
        return
    if total >= ans: return
    for i in range(2):
        y, x = r + dy[i], c + dx[i]
        if y < N and x < N:
            dfs(y, x, total + MAP[y][x])
    return

dy = [0, 1]
dx = [1, 0]

for tc in range(int(input())):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = 21e8
    dfs(0, 0, MAP[0][0])
    print('#{} {}'.format(tc+1, ans))
