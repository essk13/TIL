R = []
B = []
Y = []
G = []
total = []
color = {'R': R, 'B': B, 'Y': Y, 'G': G}
for i in range(5):
    col, num = input().split()
    num = int(num)
    color[col].append(num)
    total.append(num)
total.sort()
for i in color.keys():
    color[i].sort()

ans = 0
for i in color.keys():
    if len(color[i]) == 5:
        for n in range(4):
            if color[i][n] + 1 != color[i][n+1]:
                break
        else:
            ret = color[i][-1] + 900
            ans = max(ret, ans)
        ret = color[i][-1] + 600
        ans = max(ret, ans)

for i in range(4):
    if total[i] + 1 != total[i+1]:
        break
else:
    ret = total[-1] + 500
    ans = max(ret, ans)

cnt2 = []
cnt3 = []
for i in range(1, 10):
    if total.count(i) == 4:
        ret = i + 800
        ans = max(ret, ans)
    elif total.count(i) == 3:
        cnt3.append(i)
        ret = i + 400
        ans = max(ret, ans)
    elif total.count(i) == 2:
        cnt2.append(i)
        ret = i + 200
        ans = max(ret, ans)

if cnt2 and cnt3:
    ret = cnt3[0] * 10 + cnt2[0] + 700
    ans = max(ret, ans)

if len(cnt2) == 2:
    ret = cnt2[1] * 10 + cnt2[0] + 300
    ans = max(ret, ans)

ret = total[-1] + 100
ans = max(ret, ans)

print(ans)
