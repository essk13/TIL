# def f(lv):
#    '''
#    * 중복 순열 함수 *
#    '''
#     if lv == N:
#         print(p)
#         return
#     for i in range(1, 7):
#         p[lv] = i
#         f(lv+1)

###########################

def f(lv):
    '''
    * 순열 함수 *
    '''
    if lv == N:
        print(p)
        return
    for i in range(1, 7):
        if u[i] == 0:
            u[i] = 1
            p[lv] = i
            f(lv+1)
            u[i] = 0


N = int(input())
p = [0] * N
u = [0] * 7
#f(N, 0)
f(0)
