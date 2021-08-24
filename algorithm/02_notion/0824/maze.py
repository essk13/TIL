def dfs(y,x):
    global ans
    if MAP[y][x] == '1' or ans == 1: return         # 가지치기 (이후 재귀호출 제거)
    if MAP[y][x] == '3':
        ans = 1
    if visited[y][x] == 1 : return      # 가지치기 (이후 재귀호출 제거)
    visited[y][x] = 1
    if 0 <= y-1:
        dfs(y-1,x)
    if y+1 < N:
        dfs(y+1,x)
    if 0 <= x-1:
        dfs(y,x-1)
    if x+1 < N:
        dfs(y,x+1)
    return


T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [list(input().rstrip()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    st = []
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == '2':
                st.append(int(y))
                st.append(int(x))
                break
        if st:
            break
    ans = 0
    dfs(st[0], st[1])
    print('#{} {}'.format(tc+1, ans))