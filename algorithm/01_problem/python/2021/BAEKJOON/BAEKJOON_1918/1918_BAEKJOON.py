import sys
input = sys.stdin.readline


def bracket():
    global e
    e += 1
    i_stack = []
    while expression[e] != ')':
        E = expression[e]
        if E == '(':
            bracket()
            continue

        elif E in ('-', '+'):
            if i_stack == []:
                i_stack.append(E)
            else:
                while i_stack:
                    print(i_stack.pop(), end='')
                i_stack.append(E)

        elif E in ('*', '/'):
            if i_stack == []:
                i_stack.append(E)
            elif i_stack[-1] in ('*', '/'):
                print(i_stack.pop(), end='')
                i_stack.append(E)
            else:
                i_stack.append(E)

        else:
            print(E, end='')

        e += 1

    e += 1

    while i_stack:
        print(i_stack.pop(), end='')


expression = list(input().strip())
operator = ['+', '-', '*', '/']

stack = []

e = 0
while e < len(expression):
    E = expression[e]
    if E == '(':
        bracket()
        continue

    elif E in operator:
        if E in ('-', '+'):
            if stack == []:
                stack.append(E)
            else:
                while stack:
                    print(stack.pop(), end='')
                stack.append(E)

        else:
            if stack == []:
                stack.append(E)
            elif stack[-1] in ('*', '/'):
                print(stack.pop(), end='')
                stack.append(E)
            else:
                stack.append(E)

    else:
        print(E, end='')

    e += 1

while stack:
    print(stack.pop(), end='')
