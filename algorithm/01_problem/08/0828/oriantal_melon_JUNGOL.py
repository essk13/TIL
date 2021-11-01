K = int(input())
line = [0] * 12
for i in range(6):
    x, y = map(int, input().split())
    line[i], line[i+6] = y, y

mx = line.index(max(line))

if line[mx-1] < line[mx+1]:
    mx += 1

s1 = line[mx] * line[mx-1]
s2 = line[mx+2] * line[mx+3]
ans = s1 - s2
print(ans)
