import sys
from collections import defaultdict
sys.stdin = open('input.txt')

id_list = input().split()
users = dict(zip(id_list, range(len(id_list))))
answer = [0] * len(id_list)
reported = defaultdict(lambda: set())

for _ in range(5):
    r, red = input().split()
    reported[red].add(r)

k = int(input())
for red in reported:
    if len(reported[red]) >= k:
        res = list(reported[red])
        for r in res:
            answer[users[r]] += 1

print(answer)
