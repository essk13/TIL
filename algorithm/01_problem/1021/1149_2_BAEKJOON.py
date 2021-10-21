import sys
I = sys.stdin.readline

N = int(I())
n = [list(map(int, I().split())) for _ in range(N)]

for i in range(N-1):
    n[i+1][0] += min(n[i][1], n[i][2])
    n[i+1][1] += min(n[i][0], n[i][2])
    n[i+1][2] += min(n[i][0], n[i][1])
print(min(n[-1]))