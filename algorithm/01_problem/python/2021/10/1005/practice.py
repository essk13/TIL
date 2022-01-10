class abc:
    def __init__(self, h, w):
        self.height = h
        self.weight = w


def lst_p():
    for i in range(6):
        print(lst[i].height, lst[i].weight)
    print('-----------------------')


def m_sort(p):
    return(-p.height, p.weight)


p1 = abc(183, 89)
p2 = abc(182, 73)
p3 = abc(180, 92)

#  lst = [My_Type(180, 77) for _ in range(10)] != [My_Type(180, 77)] * 10
lst = [abc(180, 67), abc(170, 55), abc(180, 65), abc(180, 55), abc(165, 55), abc(170,40)]
lst_p()
lst.sort(key=m_sort)
lst_p()
lst.sort(key=lambda x:(x.height, -x.weight))
lst_p()