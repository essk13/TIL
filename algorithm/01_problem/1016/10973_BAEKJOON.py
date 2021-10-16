N = int(input())
p = list(map(int, input().split()))
for i in range(N-1, 0, -1):
    if p[i] < p[i-1]:
        for j in range(N-1, i-1, -1):
            if p[i-1] > p[j]:
                p[i-1], p[j] = p[j], p[i-1]
                p = p[:i] + sorted(p[i:], reverse=True)
                print(*p)
                break
        else: continue
        break
else:
    print(-1)
