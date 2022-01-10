'''
햄버거 다이어트
'''

def cook(n, kcal):
    '''
    제한 칼로리 내에서 조합한 햄버거 중
    가장 높은 점수를 반환하는 함수
    '''
    # 사용한 재료 체크
    visited[n] = 1
    score = 0
    kcal += ingredient[n][1]
    
    # 칼로리가 제한 범위를 벗어나면 점수 0 반환
    # 사용한 재료에서 제거
    if kcal > L:
        visited[n] = 0
        return score

    # 칼로리가 제한 범위를 벗어나지 않으면 점수 추가
    if kcal <= L:
        score = ingredient[n][0]
        max_s = score
    
    # 본인과 이전 조합의 중복 제거를 위해 n+1 ~ N 까지의 재료 조합
    for i in range(n+1, N):
        
        # 사용하지 않은 재료인 경우 재귀 함수 호출
        if visited[i] == 0:
            ret = cook(i, kcal)
            
            # 결과값에 본인 점수를 더해서 최고점보다 크다면 최고점 갱신
            if score + ret > max_s:
                max_s = score + ret

    #사용한 재료에서 제거
    visited[n] = 0

    #최고점 반환
    return max_s


T = int(input())
for tc in range(T):
    N, L = map(int, input().split())
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    visited = [0] * N
    
    # 각 재료를 기준으로 조합 가능한 최고점 계산
    for i in range(N):
        ans = cook(i, 0)
        if ans > max_score:
            max_score = ans

    print('#{} {}'.format(tc+1, max_score))