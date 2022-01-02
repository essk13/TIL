for tc in range(int(input())):
    s, arr = input().split()
    print('#{}'.format(tc+1), end=' ')
    for i in range(len(arr)):
        ret = int(arr[i], 16)
        ret = str(bin(ret))[2:]
        if len(ret) != 4:
            c = 4 - len(ret)
            ret = ('0' * c) + ret
        print(ret, end='')
    print()
