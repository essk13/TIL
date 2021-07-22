# all 함수
def all_function(elements):
    # elements가 빈 리스트의 경우
    if elements == list():
        return True
    # elements가 빈 리스트가 아닌 경우
    for n in elements:
        # 리스트 값 중 빈 리스트가 있거나 False가 있는 경우
        if n == list() or False:
            return False
        # 리스트 값이 모두 True인 경우
        else:
            return True

print(all_function([]))
print(all_function([1, 2, 5, '6']))
print(all_function([[], 2, 5, '6']))