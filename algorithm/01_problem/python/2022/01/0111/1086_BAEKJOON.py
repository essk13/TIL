import sys, math
from itertools import permutations
input = sys.stdin.readline
'''
Fail
'''

def check(per):
    res = 0
    while per:
        num = int(''.join(per.pop()))
        if num % K == 0:
            res += 1
    return res


def irreducible(a, b):
    mod = math.gcd(a, b)
    a //= mod
    b //= mod
    return a, b


N = int(input())
arr = []
for _ in range(N):
    arr.append(input().strip())

K = int(input())

total = math.factorial(N)
ans = 0
permutation = list(permutations(arr, N))
res = check(permutation)
ans += res

if total == ans:
    total = ans = 1
elif ans == 0:
    ans = 0
    total = 1
else:
    ans, total = irreducible(ans, total)
print('{}/{}'.format(ans, total))
