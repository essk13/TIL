import sys
sys.stdin = open('12445.txt', 'r')
'''
Baby Gin
Baby Gin
Lose
Baby Gin
Baby Gin
'''

T =int(input())
for tc in range(T):
    card = list(map(int, list(input().rstrip())))
    num_cnt = [0] * 10
    # 숫자 카드의 개수 확인
    for i in range(6):
        num = card[i]
        num_cnt[num] += 1

    score = 0
    n = 0
    while n < 10:
        # 3 보다 큰 경우 3장 제거 및 점수 += 1
        if num_cnt[n] >= 3:
            num_cnt[n] -= 3
            score += 1
            # 해당 숫자카드가 6장인 경우 한 번 더 검사해야 함으로 아래 항목 무시
            continue

        if n + 2 < 10:
            # 연속된 3개의 숫자카드의 수가 1장 이상이라면 제거 및 점수 += 1
            if num_cnt[n] > 0 and num_cnt[n+1] > 0 and num_cnt[n+2] > 0:
                num_cnt[n] -= 1
                num_cnt[n+1] -= 1
                num_cnt[n+2] -= 1
                score += 1
                # 해당 숫자카드가 2장인 경우 한 번 더 검사해야 함으로 아래 항목 무시
                continue

        n += 1

    # 점수가 2점이면 Baby Gin / 아니라면 Lose
    if score == 2:
        print('#{} Baby Gin'.format(tc+1))
    else:
        print('#{} Lose'.format(tc+1))