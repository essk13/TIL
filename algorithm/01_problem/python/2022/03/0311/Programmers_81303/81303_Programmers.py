import sys
sys.stdin = open('input.txt')
'''
PASS
'''


n, k = map(int, input().split())
cmd = list(input().split(','))

now = k
table = {i: [i - 1, i + 1] for i in range(n)}
table[0] = [None, 1]
table[n-1] = [n - 2, None]
ans = ['O'] * n
delete = []
for c in cmd:
    if c == 'C':
        ans[now] = 'X'
        delete.append(now)
        pre, nxt = table[now]
        if nxt == None:
            now = pre
        else:
            now = nxt

        if pre == None:
            table[nxt][0] = pre
        elif nxt == None:
            table[pre][1] = nxt
        else:
            table[pre][1] = nxt
            table[nxt][0] = pre

    elif c == 'Z':
        re = delete.pop()
        pre, nxt = table[re]
        ans[re] = 'O'
        if pre == None:
            table[nxt][0] = re
        elif nxt == None:
            table[pre][1] = re
        else:
            table[pre][1] = re
            table[nxt][0] = re

    else:
        c1, c2 = c[0], int(c[2])
        print(c[0], end='\n')
        print(c[1], end='\n')
        print(c[2])
        if c1 == 'D':
            to = 1
        else:
            to = 0

        for _ in range(c2):
            now = table[now][to]

print(''.join(ans))
