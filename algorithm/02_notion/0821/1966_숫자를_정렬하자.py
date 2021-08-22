import sys
sys.stdin = open('1966.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(N):
        for j in range(N-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    print('#{}'.format(tc+1), end= ' ')
    print(*num)