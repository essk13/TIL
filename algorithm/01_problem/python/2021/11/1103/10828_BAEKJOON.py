import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        stack.append(int(cmd[1]))

    else:
        if cmd[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)

        elif cmd[0] == 'size':
            print(len(stack))

        elif cmd[0] == 'empty':
            if stack: print(0)
            else: print(1)

        else:
            if stack: print(stack[-1])
            else: print(-1)
