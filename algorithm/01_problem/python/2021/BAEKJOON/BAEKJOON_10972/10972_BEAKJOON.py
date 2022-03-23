import sys

N = int(sys.stdin.readline())
ck = list(map(int, sys.stdin.readline().split()))

idx = -1
for i in range(N-1):
    if ck[i] < ck[i+1]:
        idx = i

if idx == -1:
    print(idx)
else:
    for j in range(N-1, -1, -1):
        if ck[j] > ck[idx]:
            ck[j], ck[idx] = ck[idx], ck[j]
            ans = ck[:idx+1] + sorted(ck[idx+1:])
            break
    print(*ans)
