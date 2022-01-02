D, K = map(int, input().split())
tteok = [0] * (D + 1)
tteok[1] = 'a'
tteok[2] = 'b'
for day in range(3, D+1):
    tteok[day] = tteok[day-1] + tteok[day-2]

a = tteok[D].count('a')
b = tteok[D].count('b')
A = 0
B = 0
for i in range(1, K):
    for j in range(i+1, K):
        if i + j > K:
            break
        ans = 0
        ans += i * a
        ans += j * b
        if ans == K:
            A = i
            B = j
            break
    if A:
        break

print(A)
print(B)
