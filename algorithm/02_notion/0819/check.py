dic = {
    ')': '(',
    '}': '{'
}

T = int(input())
for tc in range(T):
    N = input()
    st = []
    ans = 1

    for i in range(len(N)):
        if N[i] == '(' or N[i] == '{':
            st.append(N[i])

        elif N[i] == ')' or N[i] == '}':
            if len(st) == 0 or st.pop() != dic[N[i]]:
                ans = 0
                break

    if st:
        ans = 0

    print('#{} {}'.format(tc+1, ans))