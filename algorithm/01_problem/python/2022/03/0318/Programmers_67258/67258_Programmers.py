import sys
from collections import defaultdict
sys.stdin = open('input.txt')

for tc in range(int(input())):
    gems = list(input().split())

    gem_list = set(gems)
    gnt = len(gem_list)
    total = len(gems)
    gem_dict = defaultdict(lambda: 0)

    min_ = 100000
    ans = [0, 0]
    edn = 0
    for stn, gem in enumerate(gems):
        while len(gem_dict) < gnt and edn < total:
            gem_dict[gems[edn]] += 1
            edn += 1

        if len(gem_dict) == gnt and min_ > edn - stn:
            min_ = edn - stn
            ans = [stn + 1, edn]

        gem_dict[gem] -= 1
        if gem_dict[gem] == 0:
            del(gem_dict[gem])
    print(ans)
