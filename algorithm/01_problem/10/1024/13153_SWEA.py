import sys
sys.stdin = open('13153.txt', 'r')

idx = [1, 1, 1]
ugly = [1] * 1501
now = 2
while now < 1501:
    num1 = 2 * ugly[idx[0]]
    num2 = 3 * ugly[idx[1]]
    num3 = 5 * ugly[idx[2]]
    lst = [num1, num2, num3]
    ugly[now] = min(lst)

    for i in range(3):
        if lst[i] == ugly[now]:
            idx[i] += 1
    now += 1

for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = ugly[nums[i]]

    print('#{} {}'.format(tc+1, ' '.join(map(str, ans))))


#1 1 10 12
#2 1536
#3 216 131220000 984150 38400000 512000 398131200 637729200 566231040 576 48828125
#4 1200 640 250 10 405 150 250 360 750 768
#5 60 15 25 54 45 48 25 75 10 12