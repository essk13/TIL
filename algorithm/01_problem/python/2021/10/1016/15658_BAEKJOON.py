def cal(lv, ret):
    if lv == N:
        ans[0] = max(ans[0], ret)
        ans[1] = min(ans[1], ret)
        return
    for i in range(4):
        if o[i] > 0:
            o[i] -= 1
            if i == 0:
                cal(lv+1, ret + nums[lv])
            elif i == 1:
                cal(lv+1, ret - nums[lv])
            elif i == 2:
                cal(lv+1, ret * nums[lv])
            elif i == 3:
                if ret < 0:
                    cal(lv+1, -(abs(ret) // nums[lv]))
                else:
                    cal(lv+1, ret // nums[lv])
            o[i] += 1
    return


N = int (input())
nums = list(map(int, input().split()))
o = list(map(int, input().split()))
ans = [-21e8, 21e8]
cal(1, nums[0])
print('\n'.join(map(str, ans)))
