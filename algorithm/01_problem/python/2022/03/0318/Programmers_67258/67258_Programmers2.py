import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    gems = list(input().split())
    list_g = list(set(gems))
    stn = len(list_g)
    edn = len(gems)

    ans = [1, edn]
    st = 0
    ed = stn
    if stn == 1:
        print([1, 1])
    else:
        while st <= edn - stn + 1:
            dict_g = dict(zip(list_g, [0] * stn))
            cnt = 0
            while st < edn - 1 and gems[st] == gems[st+1]:
                st += 1
                ed += 1
            sdx = st
            edx = ed
            stop = False
            while edx <= edn + 1:
                for i in range(sdx, edx):
                    if dict_g[gems[i]] == 0:
                        dict_g[gems[i]] = 1
                        cnt += 1
                if cnt == stn:
                    if ans[1] - ans[0] > edx - st:
                        ans = [st + 1, edx]
                        stop = True
                if stop:
                    break

                sdx = edx
                edx += 1
            st += 1
            ed += 1

        print(ans)
