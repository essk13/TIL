from collections import deque
def moo(video):
    queue = deque()
    queue.append(video)
    cnt = 0
    while queue:
        now = queue.popleft()
        for x in range(len(USADO[now])):
            if USADO[now][x][1] >= k and used[USADO[now][x][0]] == 0:
                used[USADO[now][x][0]] = 1
                queue.append(USADO[now][x][0])
                cnt += 1
    return cnt


N, Q = map(int, input().split())
USADO = [[] for _ in range (N+1)]
for i in range(N-1):
    p, q, r = map(int, input().split())
    USADO[p].append([q, r])
    USADO[q].append([p, r])

for j in range(Q):
    k, v = map(int, input().split())
    used = [0] * (N+1)
    used[v] = 1
    ans = moo(v)
    print(ans)