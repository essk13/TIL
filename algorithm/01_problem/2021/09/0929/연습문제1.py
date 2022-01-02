arr = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(0, len(arr), 7):
    n = arr[i:i+7]
    ret = 0
    st = 1
    for j in range(6, -1, -1):
        ret += st * int(n[j])
        st *= 2
    if i == len(arr) - 7:
        print(ret)
        continue
    print(ret, end=', ')


for i in range(0, len(arr), 7):
    ret = int(arr[i:i+7], 2)
    if i == len(arr) - 7:
        print(ret)
        continue
    print(ret, end=', ')
