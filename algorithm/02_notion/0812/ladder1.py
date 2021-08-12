def ladder():
    c = input()
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for x in range(1, 101):
        i = x
        y = 0
        if ladder[y][x] == 1:
            while y < 99:
                while y < 99 and ladder[y][x-1] != 1 and ladder[y][x+1] != 1:
                    y += 1

                if y < 99 and ladder[y][x-1] == 1:
                    while ladder[y][x-1] == 1:
                        x -= 1
                    y += 1

                elif y < 99 and ladder[y][x+1] == 1:
                    while ladder[y][x+1] == 1:
                        x += 1
                    y += 1

        if ladder[y][x] == 2:
            return (i - 1)

test_case = 10

for case in range(test_case):
    print('#{} {}'.format(case+1, ladder()))