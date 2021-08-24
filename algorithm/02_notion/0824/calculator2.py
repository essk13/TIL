def postfix_notation(infix):
    '''
    중위 표기법을 후위 표기법으로 변환하는 함수
    '''
    st = []
    postfix = ''
    for j in range(len(infix)):
        code = infix[j]
        # 코드가 ')'라면 '('가 나올 때 까지 스택 pop 및 postfix에 추가
        if code == ')':
            while st[-1] != '(':
                postfix += st.pop()
            # '('는 pop, 출력X
            st.pop()
        # 연산자가 아닌 경우 postfix에 추가
        elif ord('0') <= ord(code) <= ord('9'):
            postfix += code
        # '('라면 스택에 push
        elif code == '(':
            st.append(code)
        # 스택이 비어있다면 코드 push
        elif not st:
            st.append(code)
        # 스택의 top보다 우선순위가 높다면 push
        elif post[code] > post[st[-1]]:
            st.append(code)
        # 스택의 top보다 우선순위가 높지 않다면 top의 우선순위가 코드보다 낮아질 때 까지 pop 및 postfix에 추가
        elif st and post[code] <= post[st[-1]]:
            while st and post[code] <= post[st[-1]]:
                postfix += st.pop()
            # pop 완료 후 스택에 push
            st.append(code)
    # 스택에 남아있는 연산자를 postfix에 추가
    if st:
        for i in range(len(st)):
            postfix += st.pop()
    # 후위 표기법 리턴
    return postfix


def calculator(postfix):
    '''
    후위 표기법을 계산하는 함수
    '''
    st = []
    for i in range(len(postfix)):
        code = postfix[i]
        # 코드가 연산자가 아니라면 스택에 push
        if ord('0') <= ord(code) <= ord('9'):
            st.append(int(code))
        # 스택이 비어있지 않으면
        elif st:
            # 2 항목을 pop
            b = st.pop()
            a = st.pop()
            # 연산자에 따라 +, -, *, / 연산 실행 후 결과를 스택에 push
            if code == '+':
                st.append(a + b)
            elif code == '-':
                st.append(a - b)
            elif code == '*':
                st.append(a * b)
            elif code == '/':
                st.append(a / b)
    # 연산이 종료된 후 결과값 pop 및 출력
    ret = st.pop()
    return ret


# 연산자의 우선순위를 딕셔너리로 저장
notation = ['+', '-', '*', '/', '(']
num = [1, 1, 2, 2, 0]
post = dict(zip(notation, num))

T = 10
for tc in range(T):
    N = int(input())
    infix = input()
    postfix = postfix_notation(infix)
    ans = calculator(postfix)

    print('#{} {}'.format(tc+1, ans))