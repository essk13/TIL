test_case = int(input())

for case in range(test_case):
    N = int(input())
    cards = list(map(int, input()))

    cnt = [0]*10

    for idx in range(N):
        cnt[cards[idx]] += 1

    max_cards = 0
    cnt_num = 0
    for i in range(10):
        if cnt[i] >= max_cards:
            max_cards = cnt[i]
            cnt_num = i

    print('#{} {} {}'.format(case+1, cnt_num, max_cards))