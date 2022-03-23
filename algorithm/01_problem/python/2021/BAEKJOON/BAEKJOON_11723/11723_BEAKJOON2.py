import sys
sys.stdin = open('input.txt', 'r')

S = 0
M = int(input())
for i in range(M):
    p = sys.stdin.readline().split()
    cmd = p[0]
    if cmd == 'all': S = (1 << 21) - 1
    elif cmd == 'empty': S = 0
    else:
        x = int(p[1])
        if cmd == 'add': S |= (1 << x)
        elif cmd == 'remove': S &= ~(1 << x)
        elif cmd == 'check':
            if S & (1 << x): print(1)
            else: print(0)
        elif cmd == 'toggle': S ^= (1 << x)
