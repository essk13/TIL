from collections import deque

N, K = map(int, input().split())
ck = [1] * 100001
ck[N] = 0
qu = deque([(N, 0)])
while qu:
    n, sec = qu.popleft()
    if n == K:
        print(sec)
        break

    if n-1 >= 0 and ck[n-1]:
        ck[n-1] = 0
        qu.append((n-1, sec+1))
    if n+1 < 100001 and K > n and ck[n+1]:
        ck[n+1] = 0
        qu.append((n+1, sec+1))
    if n*2 < 100001 and K > n and ck[n*2]:
        ck[n*2] = 0
        qu.append((n*2, sec+1))
