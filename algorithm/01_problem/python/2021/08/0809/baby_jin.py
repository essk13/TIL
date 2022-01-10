def baby_gin():
    cards = list(map(int, input().strip()))
    cnt = [0] * 10

    for card in cards:
        cnt[card] += 1

    b_ru = b_tri = idx = 0
    while idx < 10:
        if cnt[idx] >= 3:
            b_tri += 1
            cnt[idx] -= 3
            continue
        if idx > 7:
            pass
        elif cnt[idx] >= 1 and cnt[idx+1] >= 1 and cnt[idx+2] >= 1:
            b_ru += 1
            cnt[idx] -= 1
            cnt[idx+1] -= 1
            cnt[idx+2] -= 1
            continue
        idx += 1

    if b_ru + b_tri == 2:
        return 'Baby Gin'
    else:
        return 'Lose'

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, baby_gin()))