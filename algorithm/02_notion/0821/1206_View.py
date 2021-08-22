import sys
sys.stdin = open('1206.txt', 'r')

T = 10
for tc in range(T):
    N = int(input())
    building = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-2):
        now = building[i]
        # 현재 빌딩 좌, 우로 각각 2개의 빌딩과 높이 비교
        other = [building[i-2], building[i-1], building[i+1], building[i+2]]
        max_b = 0
        # 좌, 우 총 4개의 빌딩 중 가장 높은 빌딩 확인
        for j in range(4):
            if other[j] > max_b:
                max_b = other[j]
        # 현재 빌딩이 좌, 우 4개의 빌딩보다 높다면 그 차이만큼 답에 추가
        if now > max_b:
            ans += (now - max_b)

    print('#{} {}'.format(tc+1, ans))