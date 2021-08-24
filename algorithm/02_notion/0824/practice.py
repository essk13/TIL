# def dfs(lv):
#     if lv == N:
#         print(*ans)
#         return
#     for i in range(1, 5):
#         # 눈금이 사용되지 않은 경우 재귀 호출
#         if used[i] == 0:
#             ans[lv] = i
#             used[i] = 1
#             dfs(lv+1)
#             ans[lv] = 0
#             used[i] = 0
#     return
#
# # 주사위를 N 개 던질 때 중복된 눈금이 안나오는 경우 출력
# # 주사위 눈금은 1~4
# N = int(input())
# used = [0]*5
# ans = [0]*N
# dfs(0)

# arr = ['A', 'B', 'C', 'D']
#
#
# def dfs(level, path):
#     if level == 4:
#         ans = ""
#         for i in range(4):
#             if path[i] == 'O':
#                 ans += arr[i]
#         print("{} -> {}".format(path, ans))
#         return
#
#     dfs(level + 1, path + "O")
#     dfs(level + 1, path + "X")
#     return
#
#
# dfs(0, "")

def dfs(st, ed, path):
    global cnt
    if st == ed:
        cnt += 1
        print(path + str(st))
        return
    for i in range(4):
        if MAP[st][i] == 1 and visited[st] == 0:
            visited[st] = 1
            dfs(i, ed, path + str(st))
            visited[st] = 0
    return


MAP = [[0] * 4 for _ in range(4)]
path = 7
for i in range(path):
    y, x = map(int, input().split())
    MAP[y][x] = 1
visited = [0] * 4
cnt = 0
st, ed = map(int, input().split())
res = dfs(st, ed, '')
print(cnt)