from collections import deque

T = 10
for tc in range(T):
    case = '#' + input()
    num = list(map(int, input().split()))
    queue = deque()     # 큐 생성

    for i in range(8):  # 큐에 원본 배열 삽입
        queue.append(num[i])

    while queue[-1] != 0:
        for i in range(1, 6):   # 한 사이클마다 각 머리를 1 ~ 5 차감하여 꼬리로 이동 반복
            ret = queue.popleft()
            ret -= i
            if ret <= 0:        # 차감한 숫자가 0 이하가 되면 작업 종료
                ret = 0
                queue.append(ret)
                break
            queue.append(ret)

    print(case, end=' ')
    for j in range(8):
        if j < 7:
            print(queue.popleft(), end=' ')
        else:
            print(queue.popleft())