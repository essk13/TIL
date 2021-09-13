import math

goal = [0, 0]
target = [10, 10]
dy = goal[0] - target[0]
dx = goal[1] - target[1]
length = math.sqrt(dx ** 2 + dy ** 2)
t_rad = math.acos(dy/length)

R = 1
y = math.cos(t_rad) * R
x = math.sqrt(R ** 2 - y ** 2)
print(y, x)

py = target[0] - y
if dx < 0:
    px = target[1] + x
else:
    px = target[1] - x
print(py, px)
ball = [15, 18]
by = py - ball[0]
bx = px - ball[1]
b_rad = math.atan2(bx, by)

print(b_rad)
print(math.degrees(b_rad))

none = [1, 1]
m = (goal[0] - target[0]) / (goal[1] - target[1])
dist = abs(-m * none[1] + none[0] + m * goal[1] - goal[0]) / math.sqrt(1 + m ** 2)
if dist < R:
    print("CAN'T")
else:
    print('CAN')
print(dist)
