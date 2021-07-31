def check_boxes():
    '''
    샘플들에서 화학 물질이 있는 박스 묶음의 숫자와
    사이즈(행렬)를 크기 순으로 반환하는 함수
    '''
    size = int(input())
    samples = []
    # 샘플 (2차원 리스트) 생성
    for line in range(size):
        sample_line = list(map(int, input().split()))
        samples.append(sample_line)

    chemical_boxes = []
    checked_box = []
    x = 0
    start = 0
    while True:
        for y in range(size):
            column = 0
            row = 0

            # 이미 검사한 박스인 경우
            if [x, y] in checked_box:
                pass

            # 화학 물질이 없는 경우
            elif samples[y][x] == 0:
                pass

############# 화학 물질이 있는 경우 #############
            elif samples[y][x] != 0:
                checked_box.append([x, y])
                column += 1
                row += 1

################# 우측 박스에 화학 물질이 있는 경우
                if x + 1 < size and samples[y][x+1] != 0:

                    # 우측에 빈 박스가 올때까지 우측으로 이동
                    while x + 1 < size and samples[y][x+1] != 0:
                        x += 1
                        column += 1
                        checked_box.append([x, y])
                    
                    # 아래에 빈 박스가 올때까지 아래로 이동
                    if y + 1 < size and samples[y+1][x] != 0:
                        while y + 1 < size and samples[y+1][x] != 0:
                            y += 1
                            row += 1
                            checked_box.append([x, y])
                            for i in range(1, column):
                                checked_box.append([x-i, y]) # 아래로 이동하면서 우측에 화학물질이 있는 박스 확인

################# 우측이 빈 박스인 경우
                elif y + 1 < size and samples[y+1][x] != 0:
                    while y + 1 < size and samples[y+1][x] != 0:
                        y += 1
                        row += 1
                        checked_box.append([x, y])

            x = start

            if row == 0 and column == 0:
                pass
            else:
                chemical_boxes.append([row, column])

        start += 1
        x = start
        if start == size:
            break


    # 각 리스트의 곱으로 정렬
    chemical_boxes.sort(key=lambda x:x[0]*x[1])


    # 리스트의 곱이 같은 경우 행의 길이가 작은 순으로 정렬
    for idx in range(1, len(chemical_boxes)):
        if chemical_boxes[idx-1][0] * chemical_boxes[idx-1][1] == chemical_boxes[idx][0] * chemical_boxes[idx][1]:
            if chemical_boxes[idx-1][0] > chemical_boxes[idx][0]:
                chemical_boxes[idx-1], chemical_boxes[idx] = chemical_boxes[idx], chemical_boxes[idx-1]

    # 각 항목 순서대로 나열
    result = [len(chemical_boxes)]
    for box in chemical_boxes:
        result.append(box[0])
        result.append(box[1])
    
    result = list(map(str, result))

    return ' '.join(result)

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {check_boxes()}')