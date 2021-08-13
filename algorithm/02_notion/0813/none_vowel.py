def none_vowel():
    word = input()
    vowel = ['a', 'e', 'i', 'o', 'u']

    for char in vowel:
        word = word.replace(char, '')

    return word


T = int(input())
for tc in range(T):
    print('#{} {}'.format(tc+1, none_vowel()))