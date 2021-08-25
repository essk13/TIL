# def enQueue(n):
#     global rear
#     rear += 1
#     if rear >= 6:
#         return
#     Queue[rear] = n
#
# def deQueue():
#     global front
#     front += 1
#     return Queue[front]
#
# def is_Empty():
#     if front == rear:
#         return True
#     return False
#
#
# people = [3, 7, 5, 2, 1, 9]
# Queue = [0] * 6
# front = -1
# rear = -1
#
# enQueue(3)  # people[0]
# enQueue(7)  # people[1]
# enQueue(5)  # people[2]
# ret = deQueue()
# print(ret)
# ret = deQueue()
# print(ret)


# queue = [0,0,0,0,0,0,0,0,0,0]
# front = 0 # 데이터 나오는곳
# rear = 0 # 데이터 넣는곳
#
# queue[rear] = 3
# rear += 1
# queue[rear] = 5
# rear += 1
# queue[rear] = 7
# rear += 1
#
# ret = queue[front]
# front += 1
# ret = queue[front]
# front += 1

# queue = [3,7,2,1,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# front = 0
# rear = 5
#
# while queue[front] != 0:
#     print(queue[front], end=' ')
#     front += 1

# from collections import deque
#
# queue = deque() # queue 생성
# queue.append(3)  # rear 위치에 삽입 (enQueue)
# queue.append(2)
# queue.append(1)
# queue.append(5)
# queue.append(7)
# ret = queue[0]  # front 값 읽기 (peek)
# ret = queue.popleft() # front 값 삭제 및 출력 (deQueue)
#
# while queue:
#     ret = queue.popleft()
#     print(ret, end=' ')


# value = [0,1,1,3,2,4,5,2]
# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
#
# # from -> to [from][to]
# adj[0][1] = 1
# adj[0][2] = 1
# adj[0][3] = 1
# adj[1][4] = 1
# adj[1][5] = 1
# adj[1][6] = 1
# adj[3][7] = 1
#
# # 자식 노드의 값을 출력
# now = int(input())
# for next in range(8):
#     if adj[now][next] == 1: # next 가 자식노드
#         print(value[next],end=' ')

# from collections import deque
# value = [0,1,1,3,2,4,5,2]
# adj = [
#     [0 for _ in range(8)] for _ in range(8)
# ]
# adj[0][1] = 1
# adj[0][2] = 1
# adj[0][3] = 1
# adj[1][4] = 1
# adj[1][5] = 1
# adj[1][6] = 1
# adj[3][7] = 1
#
# visited = [0] * 8
# queue = deque()
# queue.append(0)
#
# while queue:
#     V = queue.popleft()
#     print(V, end=' ')
#     for i in range(8):
#         if adj[V][i] == 1 and visited[i] == 0:
#             visited[i] = 1
#             queue.append(value[i])

# from collections import deque
#
# adj = [
#     [0 for _ in range(5)] for _ in range(5)
# ]
#
# adj[0][1] = 1
# adj[0][2] = 1
# adj[1][3] = 1
# adj[1][4] = 1
# adj[2][1] = 1
# adj[2][3] = 1
# adj[4][2] = 1
#
#
# visited = [0,0,0,0,0]
# queue = deque()
#
# visited[0] = 1 # 큐에 재등록 방지 level 1 부터시작
# queue.append(0)
#
# while queue :
#     now = queue.popleft()
#     # 탐색 처리
#     print("{}의 level은 {}".format(now,visited[now]))
#     for next in range(5):
#         if adj[now][next] == 0 : continue
#         if visited[next] > 0 : continue # 큐에 한번이라도 등록 된적 있는가?
#         visited[next] = visited[now] + 1 # 큐에 재등록 방지 + level 같이 저장
#         queue.append(next)

