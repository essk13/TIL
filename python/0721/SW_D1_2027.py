result = '#'

for num in range(1, 5+1):
    print('{:+<5}'.format(result))
    result = '+' * num + '#'