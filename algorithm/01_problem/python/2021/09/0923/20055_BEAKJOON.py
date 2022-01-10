from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * N)

cnt = 0
stop = 0
while stop < K:
################    1 번 작 업    ###################
    nb = belt.pop()
    belt.appendleft(nb)
    nr = robot.pop()
    robot.appendleft(nr)
    if robot[N-1] == 1:
        robot[N-1] = 0

################    2 번 작 업    ###################
    for i in range(N - 2, -1, -1):
        if robot[i] and robot[i+1] == 0:
            if belt[i+1] > 0:
                robot[i], robot[i+1] = robot[i+1], robot[i]
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    stop += 1
                if i + 1 == N - 1:
                    robot[i+1] = 0

################    3 번 작 업    ###################
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            stop += 1
    cnt += 1

################    4 번 작 업    ###################
    if stop >= K:
        break

print(cnt)
