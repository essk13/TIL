T = 10
for tc in range(T):
    N, word = input().split()
    st = []

    for i in range(int(N)):
        if st and st[-1] == word[i]:
            st.pop()
        else:
            st.append(word[i])

    pwd = ''.join(st)
    print('#{} {}'.format(tc+1, pwd))