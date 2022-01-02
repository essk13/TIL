N = int(input())
num = list(map(int, input().split()))

for n in range(N):
    if num[n] >= 0:
        total = num[n]
        i = n + 1
        break

ans = total
while i < N:
    ret = total + num[i]
    if ret <= 0:
        total = 0
    else:
        total = ret
        if total > ans:
            ans = total
    i += 1


print(ans)


# arr = [None] * N
# arr[0] = num[0]
# for i in range(1, N):
#     arr[i] = max(0, arr[i-1]) + num[i]
