def intersection():
    vote = list(map(int, input().split()))
    max_sub = 0
    min_sub = 0

    # 투표 인원 > 투표 수 또는 투표 인원 == 투표 수인 경우의 최대, 최소
    if vote[0] > vote[1] + vote[2] or vote[0] == vote[1] + vote[2]:
        max_sub = min(vote[1:])

    # 투표 인원 < 투표 수인 경우의 최대, 최소
    elif vote[0] < vote[1] + vote[2]:
        max_sub = min(vote[1:])
        min_sub = (vote[1] + vote[2]) - vote[0]

    # 투표 인원 == 투표 수/2 인 경우의 최대, 최소
    else:
        max_sub = vote[0]
        min_sub = vote[0]
    
    result = [max_sub, min_sub]
    result = list(map(str, result))
    return ' '.join(result)

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {intersection()}')