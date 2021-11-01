T = int(input())
for tc in range(T):
    command = input().split()
    O_button = []
    B_button = []
    order = []
    
    # O와 B가 눌러야할 버튼을 각 버튼 리스트에 저장
    # 버튼을 눌러야 할 순서 저장
    for i in range(1, len(command), 2):
        if command[i] == 'O':
            O_button.append(int(command[i+1]))
            order.append('O')
        else:
            B_button.append(int(command[i+1]))
            order.append('B')

    cnt = 0
    O = 1
    Oi = 0
    B = 1
    Bi = 0
    od = 0
    while od < len(order):
        can = True  # 동시에 버튼을 누를 수 없음으로 한 명이 누르면 False로 초기화
        
        # O가 눌러야할 버튼이 남아있는 경우 아래 조건문 수행
        if Oi < len(O_button):
            if O_button[Oi] > O:    # 눌러야할 버튼이 현재 위치보다 크면 +1
                O += 1
            elif O_button[Oi] < O:  # 눌러야할 버튼이 현재 위치보다 작으면 -1
                O -= 1
            elif O_button[Oi] == O and order[od] == 'O' and can:    # 눌러야할 버튼 위치에 있으면서 본인 순서이면 명령 수행
                Oi += 1
                od += 1
                can = False

        # B가 눌러야할 버튼이 남아있는 경우 아래 조건문 수행
        if Bi < len(B_button):
            if B_button[Bi] > B:    # 눌러야할 버튼이 현재 위치보다 크면 +1
                B += 1
            elif B_button[Bi] < B:  # 눌러야할 버튼이 현재 위치보다 작으면 -1
                B -= 1
            elif B_button[Bi] == B and order[od] == 'B' and can:    # 눌러야할 버튼 위치에 있으면서 본인 순서이면 명령 수행
                Bi += 1
                od += 1
                can = False

        cnt += 1    # 한 번 수행할 때 마다 횟수 카운트

    print('#{} {}'.format(tc+1, cnt))
