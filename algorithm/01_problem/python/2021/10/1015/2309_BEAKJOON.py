def find(lv, cnt):
    if cnt == 7 and sum(p) == 100:
        print('\n'.join(map(str, p)))
        return True
    if lv >= 9 or sum(p) > 100: return False
    ret = find(lv+1, cnt)
    if ret: return True
    p.append(dwarf[lv])
    ret = find(lv+1, cnt+1)
    if ret: return True
    p.pop()

dwarf = [int(input()) for _ in range(9)]
dwarf.sort()
p = []
find(0, 0)
