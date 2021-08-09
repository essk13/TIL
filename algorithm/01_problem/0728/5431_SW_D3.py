def fail_students():
    students = list(map(int, input().split()))

    # 제출한 학생 리스트 생성
    pass_std = list(map(int, input().split()))

    # 학생 번호 리스트 생성 (1 ~ N)
    std_numbers = list(range(1, students[0]+1))

    # 제출한 학생 리스트에 존재하는 값을 번호 리스트에서 제거
    for std in pass_std:
        std_numbers.remove(std)

    # 제출 학생을 제거하고 남은 번호들을 string으로 변경
    fail_std = list(map(str, std_numbers))

    # join 메서드를 이용하여 반환
    return ' '.join(fail_std)

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {fail_students()}')