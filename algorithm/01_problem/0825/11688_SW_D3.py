T = int(input())
for tc in range(T):
    node = input()
    now = [1, 1]

    for i in range(len(node)):
        if node[i] == 'L':      # L을 선택하면 a / b 에서 a / a + b 로 변경
            now[1] = now[0] + now[1]
        else:                   # R을 선택하면 a / b 에서 a +b / b 로 변경
            now[0] = now[0] + now[1]

    print('#{} {}'.format(tc+1, ' '.join(map(str, now))))