def in_post(fix):
    st = []
    postfix = ''
    for i in range(len(fix)):
        no = fix[i]
        if no == ')':
            while st and st[-1] != '(':
                postfix += st.pop()
            st.pop()
        elif no not in notation:
            postfix += no
        elif no in notation:
            if st == [] or no == '(' or isp[st[-1]] < isp[no]:
                st.append(no)
            else:
                while st and icp[st[-1]] >= icp[no]:
                    postfix += st.pop()
                st.append(no)
    if st:
        for j in range(len(st)):
            postfix += st.pop()
    return postfix


notation = ['+', '-', '*', '/', '(']
num1 = [1, 1, 2, 2, 0]
num2 = [1, 1, 2, 2, 3]
icp = dict(zip(notation, num1))
isp = dict(zip(notation, num2))

T = int(input())
for tc in range(T):
    infix = input().rstrip()
    ret = in_post(infix)

    print('#{} {}'.format(tc+1, ret))