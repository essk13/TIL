import sys
sys.stdin = open('3143.txt', 'r')

T = int(input())
for tc in range(T):
    A ,B = input().split()
    cnt = 0
    i = 0
    while i <= (len(A) - len(B)):
        # A 안에 B가 몇번 들어가는지 확인
        for j in range(len(B)):
            if B[j] != A[i+j]:
                i += 1
                break
        else:
            cnt += 1
            # A = ababa B = aba 와 같은 예외를 처리하기 위해 B의 길이만큼 i 추가
            i += len(B)
    # 카운트마다 B 만큼의 타이핑을 1로 처리함으로 카운트 * B의 길이 - 1을 A의 길이에서 차감
    ans = len(A) - (cnt * (len(B) - 1))
    print('#{} {}'.format(tc+1, ans))