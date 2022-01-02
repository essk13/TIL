def base64_decoder():
    number = list(range(64))
    char = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
    ]

    base_64 = dict(zip(char, number))

    encoding = input()
    decoding = []

    # base_64 표로 디코딩 실시
    for ch in encoding:
        decoding.append(base_64[ch])

    # 해당 숫자를 2진수화 / 6자리 숫자가 아니라면 6자리가 되도록 앞에 0 추가
    for i in range(len(decoding)): # or list(map(bin, decoding))
        x_num = format(int(decoding[i]), 'b')
        if len(str(x_num)) < 6:
            x_num = ['0'] * (6 - len(str(x_num))) + list(str(x_num))
        else:
            x_num = list(str(x_num))
        decoding[i] = x_num

    # 8자리씩 분할
    decoding_byte = []
    for j in decoding:
        decoding_byte.extend(j)

    # 2진수를 10진수화하기 위해 '0b' 추가
    decoding.clear()
    char_1 = '0b'
    for n in range(0, len(decoding_byte), 8):
        for idx in range(8):
            char_1 += decoding_byte[n+idx]
        decoding.append(char_1)
        char_1 = '0b'

    # 2진수를 10진수로 변환
    for i in range(len(decoding)):
        decoding[i] = int(decoding[i], 2)

    # 숫자를 유니코드로 변환
    for i in range(len(decoding)):
        decoding[i] = chr(decoding[i])

    return ''.join(decoding)

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1} {base64_decoder()}')