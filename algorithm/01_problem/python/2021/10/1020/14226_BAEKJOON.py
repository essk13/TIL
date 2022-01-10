from collections import deque

# for i in range(2, 1001):
S = int(input())
# S = i
qu = deque([(1, 0)])
ck = dict()
ck[(1,0)] = 0
while qu:
    now, clip = qu.popleft()
    if now == S:
        print(ck[(now, clip)])
        # print('#{} {}'.format(i, ck[(now, clip)]))
        break

    if (now, now) not in ck.keys():
        ck[(now, now)] = ck[(now, clip)] + 1
        qu.append((now, now))
    if (now-1, clip) not in ck.keys():
        ck[(now-1, clip)] = ck[(now, clip)] + 1
        qu.append((now-1, clip))
    if clip and (now+clip, clip) not in ck.keys():
        ck[(now+clip, clip)] = ck[(now, clip)] + 1
        qu.append((now+clip, clip))
