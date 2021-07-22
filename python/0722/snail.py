# 달팽이는 낮 시간 동안에 기둥을 올라간다.
# 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다.
# 낮 시간 동안 올라간 거리보다는 적게 미끄러진다.
# 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 snail()을 작성하시오.

def snail(height, day, night):
    # n = 올라간 높이
    n = 0
    time = 1
    # 올라간 높이 + day
    while n < height:
        n += day
        # 올라간 높이가 목표 값 이상 달성 시 반복문 정지
        if n >= height:
            break
        # 목표 값 미달성 시 - night
        else:
            n -= night
        # 하루 지날때 마다 time + 1
        time += 1
    return time

print(snail(100, 5, 2))