def dfs(lv):
    global cnt
    if lv > N: return
    dfs(lv*2)
    cnt += 1
    if lv == 1:
        ans[0] = cnt
    elif lv == N//2:
        ans[1] = cnt
    dfs(lv*2+1)
    return

T = int(input())
for tc in range(T):
    N = int(input())
    ans = [0, 0]
    cnt = 0
    dfs(1)

    print('#{} {} {}'.format(tc+1, ans[0], ans[1]))