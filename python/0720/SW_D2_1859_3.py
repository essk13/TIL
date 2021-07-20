# 백만장자 프로젝트
def rich_pjt():
    day = int(input())
    price = list(map(int, input().split()))
    price_max = 0
    price_idex = 0
    re_index = 0
    expense = 0
    sales = 0
    items = 0
    gain = 0

    for i in range(day):
        if day == re_index:
            break

        for n in range(re_index, day):
            if price[n] > price_max:
                price_max = price[n]
                price_idex = n

        for d in range(re_index, price_idex + 1):
            if price[d] < price[price_idex]:
                expense += price[d]
                items += 1
            elif price[d] == price[price_idex]:
                sales = price[d]
                gain += (sales * items - expense)
                sales = 0
                expense = 0
                items = 0

        re_index = price_idex + 1
        price_idex = 0
        price_max = 0

    return gain

case_number = int(input())

for number in range(case_number):
    rich = rich_pjt()
    print(f'#{number + 1} {rich}')