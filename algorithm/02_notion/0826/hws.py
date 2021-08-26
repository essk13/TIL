from collections import deque

for tc in range(10):
    case = '#' + input()
    queue = deque(map(int, input().split()))

    t = 1
    while queue[-1] > 0:
        a = queue.popleft()
        queue.append(a - t)
        t = t % 5 + 1

    queue[-1] = 0
    print('{} {}'.format(case, ' '.join(map(str, queue))))
