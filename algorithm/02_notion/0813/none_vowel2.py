vowel = ['a', 'e', 'i', 'o', 'u']
is_vowel = [0 for _ in range(201)]
for i in range(5):
    val = ord(vowel[i])
    is_vowel[val] = 1

s = input()
for i in range(len(s)):
    val = ord(s[i])
    if is_vowel[val] == 0:
        print(chr(val), end='')