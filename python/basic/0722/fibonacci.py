number = int(input())
n1 = 0
n2 = 1
result = 0

for num in range(1, number + 1):
    if num > 1:
        result = n1 + n2
        n1 = n2
        n2 = result

print(result)