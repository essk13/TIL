import sys
from collections import defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline


def cal(st, ed):
    res = part[ed] - part[st-1]
    if not change:
        return res
    else:
        for num in change:
            if st <= num <= ed:
                res += change[num][1]
    return res


def chg(st, ed):
    if ed >= 0:
        res = ed - st
    else:
        res = -(st - ed)
    return res


N, M, K = map(int, input().split())
nums = [0] * (N + 1)
part = [0] * (N + 1)
for i in range(1, N + 1):
    n = int(input())
    nums[i] = n
    part[i] = part[i-1] + n

change = defaultdict(lambda: [])
for j in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        if change[b]:
            change[b][1] = chg(change[b][0], c)
        else:
            change[b] = [nums[b], 0]
            change[b][1] = chg(change[b][0], c)
    else:
        print(cal(b, c))
