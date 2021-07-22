# any 함수
def any_function(elements):
    # elements가 빈 리스트인 경우
    if elements == list():
        return False
    # elements가 빈 리스트가 아닌 경우
    for n in elements:
        # 리스트 값 중 참이 하나라도 있는 경우
        if n == True or n == list():
            return True
        # 리스트 값 중 참이 하나도 없는 경우
        else:
            return False

print(any_function([1, 2, 5, '6']))
print(any_function([[], 2, 5, '6']))
print(any_function([0]))