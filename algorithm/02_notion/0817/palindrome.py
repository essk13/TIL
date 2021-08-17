import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(T):
    case = '#' + input()
    puzzle = [input() for _ in range(100)]

    max_len = 1

    for y in range(100):
        for x in range(100):
            check = []
            for i in range(x, 100):
                check.append(puzzle[y][i])
                if check == check[::-1] and len(check) > max_len:
                    max_len = len(check)

    for x in range(100):
        for y in range(100):
            check = []
            for i in range(y, 100):
                check.append(puzzle[i][x])
                if check == check[::-1] and len(check) > max_len:
                    max_len = len(check)

    print(case, max_len)