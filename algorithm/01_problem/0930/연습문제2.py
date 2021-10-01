arr = '01D06079861D79F99F'
# arr = '0F97A3'
na = ''
for i in range(len(arr)):
    ret = int(arr[i], 16)
    ret = str(bin(ret))[2:]
    if len(ret) != 4:
        c = 4 - len(ret)
        ret = ('0' * c) + ret
    na += ret

ans = ''
for i in range(0, len(na), 7):
    ret = int(na[i:i+7], 2)
    ans += str(ret) + ', '

print(ans[:-2])