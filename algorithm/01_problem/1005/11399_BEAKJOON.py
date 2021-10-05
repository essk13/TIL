N = int(input())
p = list(map(int, input().split()))
p.sort()

ans = 0
for i in range(N):
    ans += sum(p[:i+1])

print(ans)
