import sys
sys.stdin = open('1221.txt', 'r')
# gns를 num으로 인코딩할 딕셔너리와 num을 다시 gns로 디코딩할 딕셔너리 사전 정의
gns = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
encoding = dict(zip(gns, num))
decoding = dict(zip(num, gns))

T = int(input())
for tc in range(T):
    case, N = input().split()
    GNS = input().split()
    cnt = [0] * 10
    # GNS에서 나온 각 숫자들의 개수를 카운트
    for i in range(int(N)):
        g = GNS[i]
        cnt[encoding[g]] += 1

    print(case)
    for j in range(10):
        # 각 숫자들의 개수만큼 출력
        if j == 9:
            print((decoding[j] + ' ') * (cnt[j] - 1), end=' ')
            print(decoding[j])
        else:
            print((decoding[j] + ' ') * cnt[j], end=' ')