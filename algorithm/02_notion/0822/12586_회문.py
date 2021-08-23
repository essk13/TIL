import sys
sys.stdin = open('12586.txt', 'r')

def row(x, y):
    # 해당 위치에서 가로로 회문 여부 검사 회문이면 문자열을 아니면 '' 반환
    for c in range(x, x + (M//2)):
        if word_puzzle[y][c] != word_puzzle[y][2 * x + M-c-1]:
            return ''
    return word_puzzle[y][x:x+M]


def column(x, y):
    # 해당 위치에서 세로로 회문 여부 검사 회문이 아니면 '' 반환
    for r in range(y, y + (M//2)):
        if word_puzzle[r][x] != word_puzzle[2 * y + M-r-1][x]:
            return ''
    ret = ''
    # 회문이라면 반복문을 통해 문자열을 형성 후 문자열 반환
    for r in range(y, y+M):
        ret += word_puzzle[r][x]
    return ret


def checking():
    # 글자판을 검사하면서 회문인 문자열이 나오면 해당 문자열 반환
    for y in range(N):
        for x in range(N - M + 1):
            # 세로줄을 이동하며 가로줄 검사
            ans = row(x, y)
            if ans != '':
                return ans

    for x in range(N):
        # 가로줄을 이동하며 세로줄 검사
        for y in range(N-M+1):
            ans = column(x, y)
            if ans != '':
                return ans


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    word_puzzle = [input() for _ in range(N)]
    ans = checking()

    print('#{} {}'. format(tc+1, ans))