def sunny():
    length = int(input())
    building = list(map(int, input().split()))

    sunny = 0
    for idx in range(2, length-2):
        if building[idx] > building[idx+1] and building[idx] > building[idx+2] and building[idx] > building[idx-1] and building[idx] > building[idx-2]:
            sunny += building[idx] - max([building[idx-2], building[idx-1], building[idx+1], building[idx+2]])

    return sunny

test_case = 10

for case in range(10):
    print('#{} {}'.format(case+1, sunny()))