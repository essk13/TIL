import sys
sys.stdin = open('12454.txt', 'r')

T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    station = [0] * (N + 1)
    charge = list(map(int, input().split()))
    # 충전 정류장 = 1로 표시
    for i in range(M):
        c_st = charge[i]
        station[c_st] = 1

    bus = 0
    ans = 0
    while bus < N + 1:
        # 버스가 도착지점 이상 이동 간으하면 반복 정지
        if bus + K >= N:
            break
    
        # 이동가능한 정류장을 역순으로 정렬
        st = station[bus + K:bus:-1]

        for j in range(K):
            # 충정 가능한 정류장을 만나면 해당 정류장으로 버스 이동 및 충전횟수 추가
            if st[j] == 1:
                bus += (K - j)
                ans += 1
                break
        else:
            # 이동 거리에서 충전소를 못만나면 반복 종료
            ans = 0
            break

    print('#{} {}'.format(tc+1, ans))