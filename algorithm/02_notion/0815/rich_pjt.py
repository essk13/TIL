T = int(input())
ret_pjt = [0] * T
for tc in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    buy = cnt = sell = profit = 0

    day = 0

    while day <= N - 1:
        max_val = max_idx = 0
        for i in range(day, N):
            if price[i] > max_val:
                max_val = price[i]
                max_idx = i

        for j in range(day, max_idx + 1):
            if j == max_idx:
                sell = cnt * price[j]
                profit += (sell - buy)
                buy = cnt = sell = 0
            else:
                buy += price[j]
                cnt += 1

        day = max_idx + 1

    print('#{} {}'.format(tc+1, profit))