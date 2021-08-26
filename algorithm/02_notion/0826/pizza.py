T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    number = list(range(1, M+1))
    queue = []
    num_que = []
    for i in range(N):
        queue.append(cheese.pop(0))
        num_que.append(number.pop(0))

    while len(queue) > 1:
        pizza = queue.pop(0) // 2
        num = num_que.pop(0)
        if pizza == 0 and len(cheese) != 0:
            queue.append(cheese.pop(0))
            num_que.append(number.pop(0))
        elif pizza != 0:
            queue.append(pizza)
            num_que.append(num)

    ans = num_que[0]
    print('#{} {}'.format(tc+1, ans))
