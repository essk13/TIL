import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0] * 10001
for i in range(N):
    n = int(input().strip())
    arr[n] += 1

for i in range(1, 10001):
    for j in range(arr[i]):
        print(i)