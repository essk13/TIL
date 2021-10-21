from collections import deque

A, B = map(int, input().split())
qu = deque([(A, 1)])
ans = -1
while qu:
    a, cnt = qu.popleft()
    if a == B:
        ans = cnt
        break
    a2 = a * 2
    if a2 <= B:
        qu.append((a2, cnt+1))
    a1 = int(str(a)+'1')
    if a1 <= B:
        qu.append((a1, cnt+1))
print(ans)