def flatten():
    dump = int(input())
    boxes = list(map(int, input().split()))

    for n in range(dump+1):
        max_box = 1
        max_h = 0
        min_box = 100
        min_h = 0
        for h in range(100):
            if boxes[h] > max_box:
                max_box = boxes[h]
                max_h = h
            if boxes[h] < min_box:
                min_box = boxes[h]
                min_h = h

        max_min = max_box - min_box
        boxes[max_h] -= 1
        boxes[min_h] += 1

        # if max_box == min_box or max_box -1 == min_box:
        #     break

    return max_min

test_case = 1

for case in range(test_case):
    print('#{} {}'.format(case+1, flatten()))


# def boxes_gap():
#     dump_num = int(input())
#     boxes = list(map(int, input().split()))
#     max_min_gap = 0
#
#     while dump_num > 0:
#         idx_max = boxes.index(max(boxes))
#         idx_min = boxes.index(min(boxes))
#
#         boxes[idx_max] -= 1
#         boxes[idx_min] += 1
#
#         max_min_gap = max(boxes) - min(boxes)
#
#         dump_num -= 1
#
#     return max_min_gap
#
#
# case_num = 10
#
# for case in range(case_num):
#     print('#{} {}'.format(case + 1, boxes_gap()))