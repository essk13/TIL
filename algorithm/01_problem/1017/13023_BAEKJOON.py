def friend(n, lv):
    ret = False
    if lv == 4: return True
    for f in adj[n]:
        if u[f]:
            u[f] = 0
            ret = friend(f, lv+1)
            u[f] = 1
            if ret: return ret
    return ret


N, M = map(int, input().split())
adj = [[] for _ in range(N)]
u = [1] * N
for i in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
for f in range(N):
    u[f] = 0
    ret = friend(f, 0)
    if ret:
        print(1)
        break
    u[f] = 1
else:
    print(0)
