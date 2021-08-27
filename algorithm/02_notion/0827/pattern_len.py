T = int(input())
for tc in range(T):
    string = input()
    ans = 0
    for i in range(1, len(string)):
        if string[0] == string[i]:
            if string[:10] == string[i:i+10]:
                ans = i
                break

    print('#{} {}'.format(tc+1, ans))
