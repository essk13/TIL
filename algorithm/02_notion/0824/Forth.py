def calculate(postfix):
    try:
        st = []
        for i in range(len(postfix)):
            code = postfix[i]
            if i == len(postfix) - 1 and code != '.':
                return 'error'
            if code == '.':
                if len(st) == 1:
                    return st.pop()
                else:
                    return 'error'
            elif code not in notation:
                st.append(int(code))
            else:
                b = st.pop()
                a = st.pop()
                if code == '+':
                    st.append(a+b)
                elif code == '-':
                    st.append(a-b)
                elif code == '*':
                    st.append(a*b)
                elif code == '/':
                    st.append(int(a/b))
    except:
        return 'error'

notation = ['+', '-', '*', '/']

T = int(input())
for tc in range(T):
    postfix = input().split()
    res = calculate(postfix)
    print('#{} {}'.format(tc+1, res))