T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0] + list(map(int, input().split()))

    while True:
        for i in range(1, N//2 + 1):
            if i * 2 + 1 <= N:
                if tree[i] > tree[i*2]:
                    tree[i], tree[i*2] = tree[i*2], tree[i]
                    break
                if tree[i] > tree[i*2+1]:
                    tree[i], tree[i*2+1] = tree[i*2+1], tree[i]
                    break
            elif i * 2 + 1 > N:
                if tree[i] > tree[i*2]:
                    tree[i], tree[i*2] = tree[i*2], tree[i]
                    break
        else:
            break

    ans = 0
    while N // 2 != 0:
        N //= 2
        ans += tree[N]

    print('#{} {}'.format(tc+1, ans))