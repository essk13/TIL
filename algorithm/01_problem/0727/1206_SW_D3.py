# 강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
# 이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.
# 그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
# 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
# 아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.
# A와 B로 표시된 세대의 경우는 왼쪽 조망은 2칸 이상 확보가 되었지만 오른쪽 조망은 한 칸 밖에 확보가 되지 않으므로 조망권을 확보하지 못하였다.
# C의 경우는 반대로 오른쪽 조망은 2칸이 확보가 되었지만 왼쪽 조망이 한 칸 밖에 확보되지 않았다.
 
# [제약 사항]
# 가로 길이는 항상 1000이하로 주어진다.
# 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)
# 각 빌딩의 높이는 최대 255이다.
 
# [입력]
# 입력 파일의 첫 번째 줄에는 테스트케이스의 길이가 주어진다. 그 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트케이스가 주어진다.
 
# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 조망권이 확보된 세대의 수를 출력한다.
def prospect_right():
    city_size = int(input())

    buildings = list(map(int, input().split()))
    prospect_right = 0
    # index 범위는 2 땅크기 -2 (좌, 우 건물이 없는 두칸 제거)
    for n in range(2, city_size-2):
        # 해당 index에 있는 건물의 크기를 좌우 두개의 건물과 비교하여 가장 큰지 여부 판단
        if buildings[n-2] < buildings[n] and buildings[n-1] < buildings[n]:
            if buildings[n] > buildings[n+1] and buildings[n] > buildings[n+2]:
                # index n 에 위치한 건물을 제외한 나머지 4개의 건물 중 가장 큰 건물을 index n 건물에서 차감
                # 차감한 값은 조망권 확보한 층에 추가
                if max(buildings[n-2:n]) > max(buildings[n+1:n+3]):
                    prospect_right += buildings[n] - max(buildings[n-2:n])
                else:
                    prospect_right += buildings[n] - max(buildings[n+1:n+3])

    return prospect_right

case_num = 10

for case in range(case_num):
    print(f'#{case+1} {prospect_right()}')
