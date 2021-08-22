import sys
sys.stdin = open('12464.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    num_cnt = [0] * 10
    card = list(map(int, list(input())))
    # 뽑은 카드에 적힌 숫자 누적
    for i in range(N):
        num = card[i]
        num_cnt[num] += 1

    max_num = 0
    max_cnt = 0
    for j in range(10):
        # 가장 많이 뽑힌 숫자카드를 확인
        # 뽑힌 횟수가 같다면 더 큰 숫자를 max_num에 저장
        if num_cnt[j] >= max_cnt:
            max_num = j
            max_cnt = num_cnt[j]

    print('#{} {} {}'.format(tc+1, max_num, max_cnt))