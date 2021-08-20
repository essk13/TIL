'''
틱택톰
'''

def row(c):
    '''
    가로 확인
    '''
    ret = 0
    for y in range(4):
        for x in range(4):
            if puzzle[y][x] != c and puzzle[y][x] != 'T':
                break
        else:
            ret = 1

    return ret


def column(c):
    '''
    세로 확인
    '''
    ret = 0
    for x in range(4):
        for y in range(4):
            if puzzle[y][x] != c and puzzle[y][x] != 'T':
                break
        else:
            ret = 1

    return ret


def ltor(c):
    '''
    우하 대각선 확인 
    '''
    ret = 0
    x = y = 0
    while x < 4:
        if puzzle[y][x] != c and puzzle[y][x] != 'T':
            break
        x += 1
        y += 1
    else:
        ret = 1

    return ret


def rtol(c):
    '''
    우상 대각선 확인 
    '''
    ret = 0
    x = 3
    y = 0
    while 0 <= x:
        if puzzle[y][x] != c and puzzle[y][x] != 'T':
            break
        x -= 1
        y += 1
    else:
        ret = 1

    return ret


T = int(input())
for tc in range(T):
    puzzle = [list(input()) for _ in range(4)]

    # 마지막 케이스가 아니면 한줄 공백 입력
    if tc != T-1:
        start = input()
    C = ['X', 'O']
    ans = 'Draw'

    for j in range(4):
        for i in range(2):
            if j == 0:
                ret = row(C[i])
                if ret == 1:
                    ans = C[i]

            elif j == 1:
                ret = column(C[i])
                if ret == 1:
                    ans = C[i]

            elif j == 2:
                ret = rtol(C[i])
                if ret == 1:
                    ans = C[i]

            elif j == 3:
                ret = ltor(C[i])
                if ret == 1:
                    ans = C[i]

    print('#{}'.format(tc+1), end=' ')

    # 결과가 'X'면 'X'가 승리
    if ans == 'X':
        print('X won')

    # 결과가 'Y'면 'Y'가 승리
    elif ans == 'O':
        print('O won')
        
    # 결과가 바뀌지 않았으면 무승부와 미종료 여부 비교
    elif ans == 'Draw':
        for i in range(4):
            
            # 빈 칸이 존재하면 미종료
            if '.' in puzzle[i]:
                ans = 'Game has not completed'
        print(ans)