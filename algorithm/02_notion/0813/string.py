def matching(pn):
    # for i in range(pn):
    #     if sentence[st+i] != chars[i]:
    #         return 0
    # return 1
    total = 0
    for i in range(len(sentence)-pn+1):
        cnt = 0
        for j in range(pn):
            if sentence[i + j] != chars[j]:
                break
            cnt += 1

        if cnt == pn:
            total += 1

    return total

T = 10
for tc in range(T):
    case = int(input())
    chars = input()
    sentence = input()

    ret = matching(len(chars))

    print('#{} {}'.format(case, ret))