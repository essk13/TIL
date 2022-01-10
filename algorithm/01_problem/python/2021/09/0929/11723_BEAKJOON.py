import sys
sys.stdin = open('input.txt', 'r')

S = [0] * 21
M = int(input())
for i in range(M):
    p = sys.stdin.readline().split()
    cmd = p[0]
    if cmd == 'all': S = [1] * 21
    elif cmd == 'empty': S = [0] * 21
    else:
        x = int(p[1])
        if cmd == 'add': S[x] = 1
        elif cmd == 'remove': S[x] = 0
        elif cmd == 'check':
            if S[x] == 1: print(1)
            else: print(0)
        elif cmd == 'toggle':
            if S[x] == 1: S[x] = 0
            else: S[x] = 1
