import sys
sys.stdin = open('input.txt', 'r')


def stack(cmd):
    global st
    if cmd == 'o':
        if st:
            return st.pop(-1)
        else:
            return 'empty'

    else:
        return len(st)


T = int(input())
for tc in range(T):
    N = int(input())
    st = []

    print('#{}'.format(tc+1))
    for i in range(N):
        cmd = input().split()

        if cmd[0] == 'i':
            st.append(cmd[1])

        else:
            ret = stack(cmd[0])
            print(ret)