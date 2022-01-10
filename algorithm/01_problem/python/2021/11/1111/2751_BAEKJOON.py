import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0] * N
for i in range(N):
    n = int(input().strip())
    arr[i] = n

arr.sort()
print('\n'.join(map(str, arr)))