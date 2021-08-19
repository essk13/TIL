T = int(input())
for tc in range(T):
    s = input()
    st = []
    for i in range(len(s)):
        if not st:
            st.append(s[i])
        else:
            if st[-1] == s[i]:
                st.pop()
            else:
                st.append(s[i])

    print('#{} {}'.format(tc+1, len(st)))