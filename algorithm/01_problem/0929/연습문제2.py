arr = '01D06079861D79F99F'
na = ''
for i in range(len(arr)):
    ret = int(arr[i], 16)
    ret = str(bin(ret))[2:]
    if len(ret) != 4:
        pass
    na += ret

print(na)