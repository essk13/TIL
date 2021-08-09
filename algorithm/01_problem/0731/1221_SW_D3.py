def univ_num():
    univ = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 외계 숫자와 아라비아 숫자를 각각 key, value로 갖는 딕셔너리 생성
    univ_num = dict(zip(univ, num)) # 외계 숫자를 아라비아 숫자로
    num_univ = dict(zip(num, univ)) # 아라비아 숫자를 외계 숫자로

    test_cate = input().split()
    univs = input().split()

    # 반복문과 univ_num을 이용하여 외계 숫자를 아라비아 숫자로 전환
    for i in range(len(univs)):
        univs[i] = univ_num[univs[i]]

    # .sort() 메서드를 이용하여 정렬
    univs.sort()

    # 반복문과 num_univ를 이용하여 아라비아 숫자를 외계 숫자로 전환
    for j in range(len(univs)):
        univs[j] = num_univ[univs[j]]

    return ' '.join(univs)

case_num = int(input())

for case in range(case_num):
    print(f'#{case+1}')
    print(f'{univ_num()}', end='\n')