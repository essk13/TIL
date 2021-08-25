def enQueue(n):
    '''
    큐의 꼬리 위치에 인자를 삽입하는 함수
    # 큐의 꼬리를 1 증가시킨 후 해당 위치에 n 삽입
    {n: 큐에 삽입할 인자}
    '''
    global rear
    rear += 1
    if rear >= len(Queue):
        print('is_full')
        return
    Queue[rear] = n


def deQueue():
    '''
    큐의 머리위치에 있는 인자를 제거 및 반환 하는 함수
    # 큐의 머리를 1 증가(제거)시킨 후 해당 위치를 반환
    '''
    global front
    front += 1
    if front == rear:
        print('is_empty')
        return
    return Queue[front]


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    Queue = [0] * 2000
    front = -1
    rear = -1

    for i in range(N):  # 기존 배열을 큐에 추가
        enQueue(num[i])

    for j in range(M):  # 배열 회전을 M번 실시
        ret = deQueue()
        enQueue(ret)

    ans = deQueue()  # 회전 완료 후 머리위치에 존재하는 숫자 반환
    print('#{} {}'.format(tc+1, ans))


# T = int(input())
#
# for tc in range(1,T+1):
#     N,M = map(int, input().split()) # 정수 개수, 회전수
#     temp = list(map(int,input().split()))
#     queue = [0 for _ in range(2000)]
#     front = 0
#     rear = 0
#     for i in range(len(temp)):
#         queue[rear] = temp[i]
#         rear += 1
#     de = -1
#     i = 0
#     while i < M: # 총 M 번 회전
#
#         # peek + deque
#         a = queue[front]
#         front += 1
#         # enque
#         queue[rear] = a
#         rear += 1
#         i += 1
#
#     print("#{} {}".format(tc, queue[front]))