import sys
input = sys.stdin.readline

for tc in range(int(input())):
    sentence = input().split()
    for i in range(len(sentence)):
        word = list(sentence[i])
        word.reverse()
        sentence[i] = ''.join(word)

    print(' '.join(sentence))