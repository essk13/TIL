# 다음과 같이 Encoding 을 한다.
# 1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.
# 2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.
# 입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.

# [제약사항]
# 문자열의 길이는 항상 4의 배수로 주어진다.
# 그리고 문자열의 길이는 100000을 넘지 않는다.

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스는 Encoding 된 상태로 주어지는 문자열이다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
def base64_decoder():
    list_str = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
    ]
    value = list(range(64))

    decoding_64 = dict(zip(list_str, value))

    word = list(input())
    decoding_word = []

    for i in word:
        decoding = decoding_64[i]
        decoding_word.append(decoding)

    decoding_word = list(map(int, decoding_word))
    decoding_word = list(map(bin, decoding_word))
    decoding_word = list(map(list, decoding_word))

    for word in decoding_word:
        delete1 = word.pop(0)
        delete2 = word.pop(0)

    decoding_num = []
    for word in decoding_word:
        if len(word) != 6:
            word1 = ['0'] * (6 - len(word)) + word
            decoding_num.append(word1)
        else:
            decoding_num.append(word)

    decoding_total = []
    for num in decoding_num:
        for n in range(6):
            i = num[n]
            decoding_total.append(i)

    encoding_b = []
    for j in range(0, len(decoding_total)+1, 8):
        group = '0b'
        for x in range(8):
            if x + j > len(decoding_total) - 1:
                break
            else:
                group = group + str(decoding_total[j+x])
        if group == '0b':
            break
        encoding_b.append(group)

    encoding_d = []
    for n in encoding_b:
        d = int(n, 2)
        encoding_d.append(d)

    ret_encoding = list(map(chr, encoding_d))

    for alpha in ret_encoding:
        if alpha == '.':
            print(alpha, end='\n')
        else:
            print(alpha, end='')

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1}', end=' ')
    base64_decoder()