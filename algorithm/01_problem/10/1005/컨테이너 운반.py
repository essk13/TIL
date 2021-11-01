for tc in range(int(input())):
    N, M = map(int, input().split())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))
    c.sort(reverse=True)
    t.sort(reverse=True)
    done = [0] * N
    ans = 0

    for i in range(M):
        for j in range(N):
            if done[j] == 0 and t[i] >= c[j]:
                done[j] = 1
                ans += c[j]
                break

    print('#{} {}'.format(tc+1, ans))
