s = input()
minimum = 2000
if len(s) == 1:
    minimum = 1
else:
    i = 1
    while i < len(s):
        j = 0
        zip_s = []
        while j < len(s)-1:
            cnt = 1
            while j < len(s)-1 and s[j:j+i] == s[j+i:j+i+i]:
                j += i
                cnt += 1
            if cnt != 1:
                zip_s.append(str(cnt))
            zip_s.append(s[j:j+i])

            j += i

        if len(s) - 1 > j:
            zip_s.append(s[j+i:1000])
        if len(s) - 1 == j:
            zip_s.append(s[j])
        ans = ''.join(zip_s)
        if len(ans) < minimum:
            minimum = len(ans)
        i += 1

print(minimum)

