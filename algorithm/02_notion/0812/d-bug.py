# def kfc():
#     print("K")
#     print("F")
#     print("C")
#     return
#
# # break point
# x = 1
# x = 2
# x = 3
# x = 4
# x = 5
# # run to cursor -> step over
# x = 10
# x = 20
# x = 30
# x = 40
#
# # step into
# kfc()
# print("i'm return")
# x = -1
# x = -2
# x = -3
# # finish
# x = 5
# x = 7
# x = 99


# def over():
#     for i in range(10):
#         print("#", end = '')
#     print("OVER")
#
# def into():
#     print("INTO")
#
# over() #over
# into() #into
# over()
# over()
# over()
# into()
# over()
# into()
# over()
# into()
# over()


def gogo():
    print("GOGO")
    return

def bts():
    gogo()
    print("BTS LAST")
    return

def abc():
    bts()
    gogo()
    print("ABC LAST")
    return

gogo()
abc()
bts()
print("ALL FINISH")

def abc(a) :
    return

# lst = [[0 for _ in range(10)] for _ in range(4)] # 4 x 10
# for y in range(4):
#     for x in range(10):
#         # [2][7] <- 버그 발생!
#         if y == 2 and x == 7 :
#             de = -1
#         abc(lst[y][x])