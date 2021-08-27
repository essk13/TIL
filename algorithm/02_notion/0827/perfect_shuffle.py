T = int(input())
for tc in range(T):
    N = int(input())
    card = input().split()
    if N % 2:
        half = N // 2 + 1
    else:
        half = N // 2

    ans = [0] * N
    card_1 = card[0:half]
    card_2 = card[half:1000]

    for i in range(0, half):
        ans[i*2] = card_1[i]
        if N % 2 and i < half - 1:
            ans[i*2+1] = card_2[i]
        elif N % 2 == 0:
            ans[i*2+1] = card_2[i]
    print('#{}'.format(tc+1), end=' ')
    print(*ans)
