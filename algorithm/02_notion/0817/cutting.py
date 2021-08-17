def cutting():
    lst = input()
    total = 0
    cnt = 0
    for i in range(len(lst)-1):
        if lst[i] == '(' and lst[i+1] == ')':
            total += cnt
        elif lst[i] == '(':
            cnt += 1
            total += 1
        elif lst[i] == ')' and lst[i-1] != '(':
            cnt -= 1

    return total

T = int(input())
for tc in range(T):
    print('#{} {}'.format(tc+1, cutting()))