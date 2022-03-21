import sys
from collections import defaultdict
sys.stdin = open('input.txt')


def check(m):
    m_list = list(m)
    for o in orders:
        for me in m_list:
            if me not in o:
                break
        else:
            courses[m] += 1
    return


def menu(now, total):
    if len(total) == c:
        if courses[total]:
            return
        del(courses[total])
        check(total)
        return

    for i in range(now, cnt):
        if used[i]:
            continue
        used[i] = 1
        menu(i + 1, total + order[i])
        used[i] = 0
    return


for tc in range(3):
    orders = input().split()
    course = list(map(int, input().split()))

    ans = []
    courses = defaultdict(lambda: 0)
    for n in range(len(orders)):
        od = list(orders[n])
        od.sort()
        orders[n] = ''.join(od)

    for order in orders:
        cnt = len(order)
        used = [0] * cnt
        for c in course:
            menu(0, '')

    min_ = defaultdict(lambda: 0)
    res = defaultdict(lambda: [])
    for key in courses:
        if courses[key] > 1:
            if min_[len(key)] == courses[key]:
                min_[len(key)] = courses[key]
                res[len(key)].append(key)
            elif min_[len(key)] < courses[key]:
                min_[len(key)] = courses[key]
                res[len(key)] = [key]

    for key in res:
        ans += res[key]

    ans.sort()
    print(ans)
