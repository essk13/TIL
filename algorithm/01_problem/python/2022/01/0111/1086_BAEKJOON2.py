import sys, math
input = sys.stdin.readline
'''
Fail
'''

def check(arr, k, cnt):
    res = 0
    i = -1
    for j in range(len(K) - 1):
        if k[i] != arr[i]:
            break
        i -= 1
    else:
        res = math.factorial(N - cnt)
    return res


def irreducible(a, b):
    mod = math.gcd(a, b)
    a //= mod
    b //= mod
    return a, b


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input().strip()))

K = int(input())
mod_arr = list(map(lambda x: x % K, arr))

total = math.factorial(N)
ans = 0

if total == ans:
    total = ans = 1
elif ans == 0:
    ans = 0
    total = 1
else:
    ans, total = irreducible(ans, total)
print('{}/{}'.format(ans, total))
