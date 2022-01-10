lst = [3, 2, 1, 3, 2, 5, 7, 9, 7]

# for val in range(1, 9+1):
#     cnt = 0
#     for target in lst:
#         if target == val:
#             cnt += 1
#
#     if cnt != 0:
#         print('{} : {}개'.format(val, cnt))

cnt = [0] * 10
for val in lst:
    cnt[val] += 1

for idx in range(len(cnt)):
    if cnt[idx] != 0:
        print('{} : {}개'.format(idx, cnt[idx]))