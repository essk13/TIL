number = []
for n in range(111, 1000):
    num = str(n)
    if len(num) == len(set(list(num))) and '0' not in num:
        number.append(num)

N = int(input())
for i in range(N):
    call, s, b = input().split()
    if s == '3':
        number = [call]
    elif s == '2':
        for j in range(len(number)):
            if not (call[0] == number[j][0] and call[1] == number[j][1] or\
                call[0] == number[j][0] and call[2] == number[j][2] or\
                call[1] == number[j][1] and call[2] == number[j][2]):
                number[j] = ''
        while '' in number:
            number.remove('')
    elif s == '1':
        if b == '1':
            for j in range(len(number)):
                if not ((call[0] == number[j][0] and ((call[1] == number[j][2] and call[2] not in number[j]) or (call[2] == number[j][1] and call[1] not in number[j]))) or\
                        (call[1] == number[j][1] and ((call[0] == number[j][2] and call[2] not in number[j]) or (call[2] == number[j][0] and call[0] not in number[j]))) or\
                        (call[2] == number[j][2] and ((call[0] == number[j][1] and call[1] not in number[j]) or (call[1] == number[j][0] and call[0] not in number[j])))):
                    number[j] = ''
            while '' in number:
                number.remove('')
        elif b == '2':
            for j in range(len(number)):
                if not ((call[0] == number[j][0] and call[1] == number[j][2] and call[2] == number[j][1]) or\
                        (call[1] == number[j][1] and call[0] == number[j][2] and call[2] == number[j][0]) or\
                        (call[2] == number[j][2] and call[0] == number[j][1] and call[1] == number[j][0])):
                    number[j] = ''
            while '' in number:
                number.remove('')
        else:
            for j in range(len(number)):
                if not ((call[0] == number[j][0] and call[1] not in number[j] and call[2] not in number[j]) or\
                        (call[1] == number[j][1] and call[0] not in number[j] and call[2] not in number[j]) or\
                        (call[2] == number[j][2] and call[0] not in number[j] and call[1] not in number[j])):
                    number[j] = ''
            while '' in number:
                number.remove('')
    else:
        if b == '1':
            for j in range(len(number)):
                if not ((call[0] != number[j][0] and call[0] in number[j] and call[1] not in number[j] and call[2] not in number[j]) or\
                        (call[1] != number[j][1] and call[1] in number[j] and call[0] not in number[j] and call[2] not in number[j]) or\
                        (call[2] != number[j][2] and call[2] in number[j] and call[0] not in number[j] and call[1] not in number[j])):
                    number[j] = ''
            while '' in number:
                number.remove('')
        elif b == '2':
            for j in range(len(number)):
                if not ((call[0] != number[j][0] and call[1] != number[j][1] and call[0] in number[j] and call[1] in number[j] and call[2] not in number[j]) or\
                        (call[0] != number[j][0] and call[2] != number[j][2] and call[0] in number[j] and call[2] in number[j] and call[1] not in number[j]) or \
                        (call[1] != number[j][1] and call[2] != number[j][2] and call[1] in number[j] and call[2] in number[j] and call[0] not in number[j])):
                    number[j] = ''
            while '' in number:
                number.remove('')
        elif b == '3':
            for j in range(len(number)):
                if call[0] not in number[j] or call[1] not in number[j] or call[2] not in number[j]:
                    number[j] = ''
            while '' in number:
                number.remove('')
            for j in range(len(number)):
                if call[0] == number[j][0] or call[1] == number[j][1] or call[2] == number[j][2]:
                    number[j] = ''
            while '' in number:
                number.remove('')
        else:
            for j in range(len(number)):
                if call[0] in number[j] or call[1] in number[j] or call[2] in number[j]:
                    number[j] = ''
            while '' in number:
                number.remove('')

print(len(number))
