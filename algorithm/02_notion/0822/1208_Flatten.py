import sys
sys.stdin = open('1208.txt', 'r')

T = 10
for tc in range(T):
    dump = int(input())
    box = list(map(int, input().split()))
    d_cnt = 0
    while d_cnt <= dump:
        max_h = 1
        max_idx = 0
        min_h = 100
        min_idx = 0
        # 반복문으로 최대값, 최대값 인덱스, 최소값, 최소값 인덱스 확인
        for i in range(100):
            if box[i] > max_h:
                max_h = box[i]
                max_idx = i
            if box[i] < min_h:
                min_h = box[i]
                min_idx = i
        # 결과 = 최대값과 최소값의 차이
        ans = max_h - min_h
        # 차이가 1이하라면 평탄화 완료
        if ans <= 1:
            break
        # 최대값의 하나를 최소값에 추가
        box[max_idx] -= 1
        box[min_idx] += 1
        # 덤프 횟수 1 증가
        d_cnt += 1

    print('#{} {}'.format(tc+1, ans))