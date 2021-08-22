import sys
sys.stdin = open('5789.txt', 'r')

T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    # 박스 리스트 생성
    box = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        # i번째 작업에 L ~ R번 까지의 박스 번호를 i 로 변경
        for j in range(L-1, R):
            box[j] = i

    print('#{}'.format(tc+1), *box)