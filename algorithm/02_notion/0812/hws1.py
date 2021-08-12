boxes = [1, 2, 2, 3, 4, 5, 5, 6, 8, 9, 9]

# for dump in range(5):
#     x = 0
#     y = 10
#     boxes[x] += 1
#     boxes[y] -= 1
#     while x + 1 < 11 and boxes[x] > boxes[x+1]:
#         boxes[x], boxes[x+1] = boxes[x+1], boxes[x]
#         x += 1
#
#     while 0 <= y - 1 and boxes[y] < boxes[y-1]:
#         boxes[y], boxes[y-1] = boxes[y-1], boxes[y]
#         y -= 1
#
# print (boxes[10] - boxes[0])

cnt = [0]*10
for i in boxes:
    cnt[i] += 1

for j in range(6):
    max_b = 0
    min_b = 10
    for idx in range(len(cnt)):
        if cnt[idx] != 0:
            if idx > max_b:
                max_b = idx
            if idx < min_b:
                min_b = idx

    result = max_b - min_b
    cnt[max_b] -= 1
    cnt[max_b-1] += 1
    cnt[min_b] -= 1
    cnt[min_b+1] += 1

print(result)
