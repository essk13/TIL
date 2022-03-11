import sys
sys.stdin = open('input.txt')
'''
FAIL
'''


def nxt(row):
    nn = row + 1
    while nn <= n - 1:
        if ans[nn]:
            return nn
        nn += 1

    nn = row - 1
    while nn >= 0:
        if ans[nn]:
            return nn
        nn -= 1


n, k = map(int, input().split())
cmd = list(input().split(','))

ans = [1] * n
delete = []

now = k
for c in cmd:
    if len(c) == 1:
        # Remove
        if c == 'C':
            delete.append(now)
            ans[now] = 0
            now = nxt(now)
        # Undo
        elif c == 'Z':
            pre = delete.pop()
            ans[pre] = 1

    else:
        # Up
        if c[0] == 'U':
            cnt = 0
            m = now - int(c[2])
            while sum(ans[m:now]) < int(c[2]):
                m -= 1
            now = m
        # Down
        elif c[0] == 'D':
            cnt = 0
            m = now + int(c[2])
            while sum(ans[now+1:m+1]) < int(c[2]):
                m += 1
            now = m

answer = ''
for a in ans:
    if a:
        answer += 'O'
    else:
        answer += 'X'
print(answer)
