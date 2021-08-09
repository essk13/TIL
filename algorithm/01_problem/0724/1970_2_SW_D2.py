def change_money():
    money = int(input())
    # 거스름돈 종류 리스트 생성
    change_type = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change_list = []
    # 거스름돈 종류보다 크다면 금액 - 해당 거스름돈 종류 / - 횟수 카운트 후 거스름돈 리스트에 추가
    for type_m in change_type:
        change = 0
        while money >= type_m:
            if money >= type_m:
                money -= type_m
                change += 1
        if change == 0:
            change_list.append(0)
        else:
            change_list.append(change)
    
    return change_list

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1}')
    print(*change_money())