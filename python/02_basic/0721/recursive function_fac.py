# def fact():
#     number = int(input())
#     factorial = 1
#     for num in range(1, number + 1):
#         factorial *= num
#     return factorial

# print(fact())

# def fact(n):
#     result = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     return result
    
# print(fact(4))

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(3))