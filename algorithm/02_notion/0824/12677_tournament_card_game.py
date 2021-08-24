def rsp(player1, player2):
    '''
    가위, 바위, 보 승자 확인 함수
    {1:'가위', 2:'바위', 3:'보'}
    game[player] == 플레이어의 가위/바위/보
    # 비긴 경우 1번이 승리 #
    '''
    if game[player1] == game[player2] or \
        (game[player1] == 1 and game[player2] == 3) or \
        (game[player1] == 2 and game[player2] == 1) or \
        (game[player1] == 3 and game[player2] == 2):
        return player1

    return player2

def tournament(st_i, ed_i):
    '''
    인원이 한명이 될 때 까지 두개의 그룹으로 분할하는 함수
    # 분리는 시작 + 끝 번호 // 2 를 기준으로 분할 #
    {st_i: start_index, ed_i: end_index}
    '''
    if st_i == ed_i:
        return st_i
    p1 = tournament(st_i, (st_i+ed_i)//2)
    p2 = tournament(((st_i+ed_i)//2)+1, ed_i)
    win = rsp(p1, p2)   # 1명 단위로 분할이 완료되면 각각 자신의 상대와 대결
    return win

T = int(input())
for tc in range(T):
    N = int(input())
    game = [0] + list(map(int, input().split()))    # 학생의 번호와 인덱스를 일치시키기 위해 맨 앞에 [0] 추가
    ans = tournament(1, N)
    print('#{} {}'.format(tc+1, ans))