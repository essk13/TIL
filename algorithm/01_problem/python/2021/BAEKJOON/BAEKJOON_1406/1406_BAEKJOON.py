import sys
from collections import deque
input = sys.stdin.readline

left = deque(list(input().strip()))
right = deque()
M = int(input())

for _ in range(M):
    cmd = input().split()
    if len(cmd) == 1:
        # 좌로 이동
        if cmd[0] == 'L' and left:
            right.appendleft(left.pop())
        # 우로 이동
        elif cmd[0] == 'D' and right:
            left.append(right.popleft())
        # 좌측 제거
        elif cmd[0] == 'B' and left:
            left.pop()

    else:
        left.append(cmd[1])

print(''.join(left) + ''.join(right))
