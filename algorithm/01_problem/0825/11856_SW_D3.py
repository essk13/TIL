T = int(input())
for tc in range(T):
    string = input()
    ans = 'No'

    # 첫 문자와 두 번째 문자가 다른 경우 각각의 횟수가 2이면 Yes
    if string[0] != string[1] and \
        string.count(string[0]) == 2 and \
        string.count(string[1]) ==2:
        ans = 'Yes'

    # 첫 문자와 두 번째 문자가 같으면서 세 번째 문자와 네 번째 문자가 같고
    # 첫 문자와 세 번째 문자가 다른 경우 Yes
    elif string[0] == string[1] and \
        string[0] != string[2] and \
        string[2] == string[3]:
        ans = 'Yes'

    print('#{} {}'.format(tc+1, ans))