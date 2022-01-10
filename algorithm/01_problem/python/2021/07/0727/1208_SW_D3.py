# [제약 사항]
# 가로 길이는 항상 100으로 주어진다.
# 모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.
# 덤프 횟수는 1이상 1000이하로 주어진다.
# 주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

# [입력]
# 총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.

def boxes_gap():
    dump_num = int(input())
    boxes = list(map(int, input().split()))
    max_min_gap = 0

    # 덤프 횟수만큼 반복 실시
    while dump_num > 0:

        # 가장 높은 박스의 인덱스와 가장 낮은 박스의 인덱스 호출
        idx_max = boxes.index(max(boxes))
        idx_min = boxes.index(min(boxes))

        # 최대, 최소 박스의 값을 각각 +1, -1 씩 박스 이동
        boxes[idx_max] -= 1
        boxes[idx_min] += 1

        max_min_gap = max(boxes) - min(boxes)

        # # 이동 후 가장 높은 박스의 인덱스와 가장 낮은 박스의 인덱스 호출
        # idx_max = boxes.index(max(boxes))
        # idx_min = boxes.index(min(boxes))

        # # 이동 후 최대, 최소 박스의 차이를 저장
        # max_min_gap = boxes[idx_max] - boxes[idx_min]

        # 덤프 횟수 1회 차감
        dump_num -= 1

    return max_min_gap

case_num = 10

for case in range(case_num):
    print(f'#{case+1} {boxes_gap()}')