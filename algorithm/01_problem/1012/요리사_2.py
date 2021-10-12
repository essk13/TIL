import sys
sys.stdin = open('recipe.txt', 'r')

def com(lv):
    global min_
    if lv >= N:
        return
    if sum(u) == N//2:
        sc1 = 0
        sc2 = 0
        for i in range(N):
            for j in range(N):
                if i != j:
                    if u[i] == 1 and u[j] == 1:
                        sc1 += recipe[i][j]
                    elif u[i] == 0 and u[j] == 0:
                        sc2 += recipe[i][j]
        min_ = min(min_, abs(sc1 - sc2))
        return

    u[lv] = 1
    com(lv + 1)
    u[lv] = 0
    com(lv + 1)
    return


for tc in range(int(input())):
    N = int(input())
    recipe = [list(map(int, input().split())) for _ in range(N)]
    u = [0] * N
    min_ = 21e8
    com(0)
    print('#{} {}'.format(tc+1, min_))

#1 2
#2 1
#3 38
#4 15
#5 4
#6 0
#7 51
#8 23
#9 13
#10 11
