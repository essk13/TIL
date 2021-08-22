import sys
sys.stdin = open('12554.txt', 'r')

T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split())
    st_a = 1
    ed_a = P
    c_a = int((st_a + ed_a) / 2)
    st_b = 1
    ed_b = P
    c_b = int((st_b + ed_b) / 2)
    winner = 0
    # A와 B가 동시에 탐색 시작
    while winner == 0:
        # 중앙값이 탐색값보다 크면 종료값 수정
        # 중앙값이 탐색값보다 작으면 시작값 수정
        # 탐색 완료 시 A는 +1 B는 +2 실시
        if A < c_a:
            ed_a = c_a
        elif A > c_a:
            st_a = c_a
        elif A == c_a:
            winner += 1

        if B < c_b:
            ed_b = c_b
        elif B > c_b:
            st_b = c_b
        elif B == c_b:
            winner += 2
        # 중앙값 수정
        c_a = int((st_a + ed_a) / 2)
        c_b = int((st_b + ed_b) / 2)

    # 답은 승자가 1이면 A 2면 B 둘 다 아니면 0
    if winner == 1:
        ans = 'A'
    elif winner == 2:
        ans = 'B'
    else:
        ans = 0

    print('#{} {}'.format(tc+1, ans))