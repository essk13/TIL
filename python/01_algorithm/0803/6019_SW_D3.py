def fucking_fly():
    d, train_a, train_b, fly = list(map(int, input().split()))
    
    # 기차와 기차가 충돌하기까지 걸리는 시간
    total_time = d / (train_a + train_b)
    
    # 파리가 움직인 총 시간 * 파리 속도
    fly_d = total_time * fly
    
    return fly_d

case_num = int(input())

for case in range(case_num):
    print('#{} {:.10f}'.format(case+1, fucking_fly()))