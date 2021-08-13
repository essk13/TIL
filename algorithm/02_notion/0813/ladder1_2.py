def ladder():
    c = input()
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for x in range(1, 101):
        i = x
        y = 99
        if ladder[y][x] == 2:
            while y > 0:
                while y > 0 and ladder[y][x-1] != 1 and ladder[y][x+1] != 1:
                    y -= 1

                if y > 0 and ladder[y][x-1] == 1:
                    while ladder[y][x-1] == 1:
                        x -= 1
                    y -= 1

                elif y > 0 and ladder[y][x+1] == 1:
                    while ladder[y][x+1] == 1:
                        x += 1
                    y -= 1

        if y == 0:
            return (x - 1)

test_case = 10

for case in range(test_case):
    print('#{} {}'.format(case+1, ladder()))