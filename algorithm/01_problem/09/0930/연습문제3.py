p = ['001101', '010011', '111011', '110001', '100011',
     '110111', '001011', '111101', '011001', '101111']
num = list(range(10))
enc = dict(zip(p, num))

arr = '0269FAC9A0'
# arr = '0DEC'
na = ''
for i in range(len(arr)):
    ret = int(arr[i], 16)
    ret = str(bin(ret))[2:]
    if len(ret) != 4:
        c = 4 - len(ret)
        ret = ('0' * c) + ret
    na += ret

print(na)

ed = 0
for j in range(len(na)-1, -1, -1):
    if na[j] == '1':
        ed = j
        break

pw = ''
for x in range(ed, -1, -6):
    pw = str(na[x-5:x+1]) + pw

for i in range(0, len(pw), 6):
    ret = enc[pw[i:i+6]]
    print(ret, end=' ')
