import sys
I = sys.stdin.readline

formula = I()
formula_ = []
now = []
operator = []
for i in range(len(formula)):
    if formula[i] == '+' or formula[i] == '-' or i == len(formula) - 1:
        formula_.append(int(''.join(now)))
        if operator:
            op = operator.pop()
            formula_.append(op)
        operator.append(formula[i])
        now = []
    else:
        now.append(formula[i])

stack = []
operator = []
for i in range(len(formula_)):
    if formula_[i] == '+':
        num1 = stack.pop()
        num2 = stack.pop()
        ret = num1 + num2
        stack.append(ret)
    elif formula_[i] == '-':
        operator.append(formula_[i])
    else:
        stack.append(formula_[i])

ret = stack[0]
for j in range(1, len(stack)):
    ret -= stack[j]

print(ret)