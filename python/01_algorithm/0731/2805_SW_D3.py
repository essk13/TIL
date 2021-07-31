def farm_revenue():
    '''
    농장의 최고 수익을 반환하는 함수
    '''
    farm_size = int(input())
    farm = []
    
    # 농장(2차원 리스트) 생성
    for num in range(farm_size):
        farm_line = list(map(int, list(input())))
        farm.append(farm_line)

    revenue = 0

    # y가 0 ~ 농장 사이즈의 중앙값 까지 반복될 때
    for y in range(farm_size//2+1):

######### y가 0 ~ 중앙값 전까지
        # 중앙칸을 시작으로 양쪽으로 한칸씩 수확 영역 확장
        for x in range(farm_size//2-y, farm_size//2+1+y):

            # y가 중앙값일 경우 계산 중지
            if y != farm_size//2:
                revenue += farm[y][x]
            else:
                pass

######### y가 중앙값 ~ 끝까지
        # 전체칸을 시작으로 양쪽으로 한칸씩 수확 영영 축소
        for i in range(y, farm_size-y):
            revenue += farm[y+farm_size//2][i]

    return revenue

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {farm_revenue()}')