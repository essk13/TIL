def first_char():
    N = int(input())
    lst = [x[0].upper() for x in input().split()]

    return ''.join(lst)

T = int(input())
for tc in range(T):
    print('#{} {}'.format(tc+1, first_char()))