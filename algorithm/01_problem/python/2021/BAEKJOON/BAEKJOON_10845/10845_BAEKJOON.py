import sys
input = sys.stdin.readline

N = int(input())
qu = [0] * 100000
st = ed = 0

for _ in range(N):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'pop':
            if st == ed:
                print(-1)
            else:
                print(qu[st])
                st += 1

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
                print(qu[st])

        elif cmd[0] == 'back':
            if st == ed:
                print(-1)
            else:
                print(qu[ed - 1])

    else:
        qu[ed] = cmd[1]
        ed += 1
