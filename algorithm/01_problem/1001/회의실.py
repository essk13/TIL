data = [
    [1, 6],
    [3, 8],
    [8, 9],
    [2, 4],
    [4, 6],
    [7, 9],
]

for i in range(len(data) - 1):
    for j in range(i, len(data)):
        if data[i][1] > data[j][1]:
            data[i], data[j] = data[j], data[i]
print(data)

p = [data[0]]
for x in range(1, len(data)):
    if data[x][0] >= p[-1][1]:
        p.append(data[x])

print(p)
print(len(p))