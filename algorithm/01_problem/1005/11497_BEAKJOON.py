for tc in range(int(input())):
    N = int(input())
    tr = list(map(int, input().split()))
    tr.sort()
    ret = [0] * N
    for i in range(N):
        if i % 2:
            ret[-((i//2)+1)] = tr[i]
        else:
            ret[i//2] = tr[i]
    ans = 0
    for j in range(0, N):
        if j == N-1:
            ans = max(ans, abs(ret[j] - ret[0]))
        else:
            ans = max(ans, abs(ret[j]-ret[j+1]))
    print(ans)
