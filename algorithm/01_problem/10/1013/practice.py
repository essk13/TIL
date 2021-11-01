def Find(char):
    if rep[char] == char:
        return char
    ret = Find(rep[char])
    # 추가적인 경로 압축을 통해 효율적 연산 가능
    return ret


def Union(parent, child):
    global group_cnt
    p = Find(parent)
    c = Find(child)
    if p != c:
        rep[c] = p
        group.remove(c)
        group_cnt -= 1
    print('{} 그룹이 남았습니다.'.format(group_cnt))
    return


rep = {}
group = []
group_cnt = 0
for ch in range(ord('A'), ord('Z') + 1):
    group.append(chr(ch))
    group_cnt += 1
    rep[chr(ch)] = chr(ch)

Union('A', 'B')
Union('C', 'D')
Union('D', 'A')
Union('A', 'C')
Union('K', 'G')
Union('I', 'G')
Union('H', 'I')
Union('G', 'D')

# print(Find('A'))
# print(Find('B'))
# print(Find('C'))
# print(Find('D'))
# print(Find('I'))
# print(Find('K'))
# print(Find('G'))
# print(Find('H'))
print('최종 {} 그룹이 남았습니다.'.format(group_cnt))

# rep['E'] = 'D'
# rep['D'] = 'C'
# rep['C'] = 'B'
# rep['B'] = 'A'

# print(Find('E'))
# print(Find('D'))
# print(Find('B'))
# print(Find('A'))
