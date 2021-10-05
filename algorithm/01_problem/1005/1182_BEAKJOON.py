def f(lv):
    global cnt
    if lv == N:
        if sum(p) == S:
            cnt += 1
        return
    p.append(arr[lv])
    f(lv+1)
    p.pop()
    f(lv+1)
    return


N, S = map(int, input().split())
arr = list(map(int, input().split()))
p = []
cnt = 0
f(0)
if S == 0:
    cnt -= 1
print(cnt)
