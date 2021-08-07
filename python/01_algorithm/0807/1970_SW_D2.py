def change_money():
    change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    money = int(input())
    changes = []

    for change in change_list:
        result = money // change
        changes.append(str(result))
        money -= result * change

    return ' '.join(changes)

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1}')
    print(change_money())