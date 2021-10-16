def trip(now, st, lv, total):
    global ans
    if total > ans: return
    if lv == N and now == st:
        ans = min(ans, total)
        return
    for i in range(N):
        if visited[i] and adj[now][i]:
            visited[i] = 0
            trip(i, st, lv+1, total + adj[now][i])
            visited[i] = 1
    return


N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
ans = 21e8
for i in range(N):
    visited = [1] * N
    trip(i, i, 0, 0)
print(ans)
