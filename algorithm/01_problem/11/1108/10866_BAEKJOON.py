import sys
input = sys.stdin.readline

N = int(input())
deque = [0] * 20001
st = ed = 10000

for _ in range(N):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'pop_front':
            if st == ed:
                print(-1)
            else:
                print(deque[st])
                st += 1

        elif cmd[0] == 'pop_back':
            if st == ed:
                print(-1)
            else:
                ed -= 1
                print(deque[ed])

        elif cmd[0] == 'size':
            print(ed - st)

        elif cmd[0] == 'empty':
            if st == ed:
                print(1)
            else:
                print(0)

        elif cmd[0] == 'front':
            if st == ed:
                print(-1)
            else:
                print(deque[st])

        elif cmd[0] == 'back':
            if st == ed:
                print(-1)
            else:
                print(deque[ed-1])

    else:
        if cmd[0] == 'push_front':
            st -= 1
            deque[st] = cmd[1]

        else:
            deque[ed] = cmd[1]
            ed += 1