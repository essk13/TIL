ugly = [2, 3, 5]
min_ = [1, 1, 1]
lst = [0, 0, 0]
uglies = [1] * 1501
for i in range(2, 1501):
    for j in range(3):
        lst[j] = uglies[min_[j]] * ugly[j]
    ret = min(lst[0], lst[1], lst[2])
    uglies[i] = ret
    for j in range(3):
        if lst[j] == ret:
            min_[j] += 1
    lst = [0, 0, 0]

for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = uglies[nums[i]]
    print('#{} {}'.format(tc+1, ' '.join(map(str, ans))))
