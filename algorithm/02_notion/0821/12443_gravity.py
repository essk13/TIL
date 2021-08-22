import sys
sys.stdin = open('12443.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    box = list(map(int, input().split()))
    max_drop = 0
    for i in range(N):
        cnt = 0
        # 현 위치의 박스 뒤로 높이가 더 작은 박스의 수 확인
        for j in range(i, N):
            if j != i and box[j] < box[i]:
                cnt += 1
            # 박스의 낙차는 높이가 더 작은 박수의 수 와 동일
            drop = cnt
            # 가장 큰 낙차와 현재 낙차를 비교하여 더 큰 값 저장
            if drop > max_drop:
                max_drop = drop

    print('#{} {}'.format(tc+1, max_drop))