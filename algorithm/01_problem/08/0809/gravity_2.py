def gravity():
    row = int(input())
    boxes = list(map(int, input().split()))
    height = max(boxes)

    g_boxes = []
    for i in range(row):
        x = [1] * boxes[i] + [0] * (height - boxes[i])
        g_boxes.append(x)

    max_gravity = 0
    gravity = 0
    for y in range(row-2, 0-1, -1):
        for x in range(height):
            for idx in range(1, row):
                if y + idx > row - 1:
                    break
                elif g_boxes[y+idx-1][x] != 0 and g_boxes[y+idx][x] == 0:
                    g_boxes[y+idx-1][x], g_boxes[y+idx][x] = g_boxes[y+idx][x], g_boxes[y+idx-1][x]
                    gravity += 1

            if gravity > max_gravity:
                max_gravity = gravity

            gravity = 0

    return max_gravity

test_case = int(input())

for case in range(test_case):
    print('#{} {}'.format(case+1, gravity()))