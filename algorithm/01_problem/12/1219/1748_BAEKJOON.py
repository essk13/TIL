N = int(input())
n = [-1, 0, 9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]

now = 9
ans = 0
while now >= 1:
    if N >= n[now]:
        N -= n[now]
        ans += (N * now)
        N = n[now]

    now -= 1

print(ans)