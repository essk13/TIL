def count_(j):
    cnt = 0
    while j < len(sample) and sample[j] == '1':
        if sample[j] == '1':
            cnt += 1
        j += 1
    return cnt


sample = '000011000110111011111100001100011111100001010111'
max_ = 0
min_st = len(sample)
for i in range(len(sample)):
    if i == 0 or (sample[i] == '1' and sample[i-1] =='0'):
        ret = count_(i)
        if ret == max_:
            min_st = min(min_st, i)
        elif ret > max_:
            max_ = ret
            min_st = i


print(max_, min_st)