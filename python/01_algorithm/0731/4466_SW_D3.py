def max_report():
    '''
    성적표에 총점이 가장 크게 장성되었을 경우의
    총점을 반환하는 함수
    '''
    report_size = list(map(int, input().split()))
    scores = list(map(int,input().split()))

    # 성적을 내림차순으로 정렬
    scores.sort(reverse=True)

    # 작성 가능한 과목수 까지 합 계산
    max_report = sum(scores[:report_size[1]])

    return max_report

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {max_report()}')