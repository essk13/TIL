N = int(input())

# 숫자를 문자열 형태로 저장
game = list(map(str, range(1, N+1)))

result = []
for i in range(N):
    cnt = 0
    for j in range(len(game[i])):

        # 문자열로 된 각 숫자를 하나씩 나누어 3, 6, 9에 포함되는가를 확인
        if game[i][j] in ['3','6','9']:
            cnt += 1

    # 포함된 횟수 만큼의 '-'로 숫자 변환
    if cnt != 0:
        game[i] = '-'*cnt

print(*game)