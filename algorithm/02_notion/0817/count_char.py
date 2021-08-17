def max_char():
    str1 = list(input())
    str2 = input()
    cnt = [0] * len(str1)
    dic = dict(zip(str1, cnt))

    for i in range(len(str2)):
        if str2[i] in str1:
            dic.update({str2[i]: dic[str2[i]]+1})

    max_char = 0
    for i in dic.values():
        if i > max_char:
            max_char = i

    return max_char

T = int(input())

for tc in range(T):
    print('#{} {}'.format(tc+1, max_char()))