import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

ans = 0
pre = 0
for a in arr:
    if not pre:
        pre = a[1]
        ans += 1
    elif pre <= a[0]:
        pre = a[1]
        ans += 1

print(ans)
