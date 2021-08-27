card_lst = {'S': 0, 'D': 1, 'H': 2, 'C': 3}

T = int(input())
for tc in range(T):
    now_card = input()
    N = len(now_card)
    now = []
    ans = [13] * 4
    ret = True
    for i in range(0, N, 3):
        card = now_card[i:i+3]
        ans[card_lst[card[0]]] -= 1
        now.append(card)

    if N // 3 != len(set(now)):
        ans = 'ERROR'
        ret = False

    print('#{}'.format(tc+1), end=' ')
    if ret:
        print(*ans)
    else:
        print(ans)
