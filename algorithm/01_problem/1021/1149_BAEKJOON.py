import sys
I = sys.stdin.readline

def dfs(lv, cost, color):
    global ans
    if cost >= ans: return
    if lv == N:
        ans = min(ans, cost)
        return
    for i in range(3):
        if i != color:
            dfs(lv+1, cost+n[lv][i], i)


N = int(I())
n = [list(map(int, I().split())) for _ in range(N)]
ans = 21e8
dfs(0, 0, -1)
print(ans)