# while 문 회문 판별 함수
def palindrome_while(word):
    word_list = list(word)
    word_list_reverse = []
    idx = len(word) - 1

    while idx >= 0:
        word_list_reverse.append(word_list[idx])
        idx -= 1
    
    if word_list == word_list_reverse:
        return True
    else:
        return False

print(palindrome_while('tomato'))
print(palindrome_while('racecar'))
print(palindrome_while('azza'))
print('-' * 20)

# reversed 회문 판별 함수
def palindrome_reverse(word):
    word_list = list(word)
    word_list_reverse = word_list[::-1]
    if word_list == word_list_reverse:
        return True
    else:
        return False

print(palindrome_reverse('tomato'))
print(palindrome_reverse('racecar'))
print(palindrome_reverse('azza'))
print('-' * 20)

# 재귀함수 회문 판별 함수
def palindrome_recursive(word):
    if len(word) < 2:
        return True
    elif word[0] != word[len(word) - 1]:
        return False
    else:
        return palindrome_recursive(word[1:len(word)-1])

print(palindrome_recursive('tomato'))
print(palindrome_recursive('racecar'))
print(palindrome_recursive('azza'))
