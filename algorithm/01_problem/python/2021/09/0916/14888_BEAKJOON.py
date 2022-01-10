from collections import deque

def bfs(n, num):
    queue = deque()
    queue.append([n, num, ''])
    max_ret = -21e8
    min_ret = 21e8
    while queue:
        n_n, n_num, op = queue.popleft()
        if n_n == N - 1:
            max_ret = max(max_ret, n_num)
            min_ret = min(min_ret, n_num)
        for j in range(4):
            if n_n == N - 1:
                break
            elif operators[j] != 0:
                if j == 0 and op.count('+') < operators[0]:
                    queue.append([n_n+1, n_num + nums[n_n+1], op + '+'])
                elif j == 1 and op.count('-') < operators[1]:
                    queue.append([n_n+1, n_num - nums[n_n+1], op + '-'])
                elif j == 2 and op.count('*') < operators[2]:
                    queue.append([n_n+1, n_num * nums[n_n+1], op + '*'])
                elif j == 3 and op.count('/') < operators[3]:
                    if n_num < 0:
                        t_num = -(abs(n_num) // nums[n_n+1])
                        queue.append([n_n+1, t_num, op + '/'])
                    else:
                        t_num = n_num // nums[n_n+1]
                        queue.append([n_n+1, t_num, op + '/'])
    return max_ret, min_ret


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

ans = bfs(0, nums[0])
print('{}\n{}'.format(ans[0], ans[1]))
