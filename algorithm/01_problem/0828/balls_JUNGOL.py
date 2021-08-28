N = int(input())
ball = input()
check = ball[-1]
c = False
ret = [0, 0, 0, 0]
for i in range(N-2, -1, -1):
    if ball[i] != check:
        ret[0] += 1
        c = True
    elif c and ball[i] == check:
        ret[1] += 1

check2 = ball[0]
c2 = False
for i in range(1, N):
    if ball[i] != check2:
        ret[2] += 1
        c2 = True
    elif c2 and ball[i] == check2:
        ret[3] += 1

print(min(ret))
