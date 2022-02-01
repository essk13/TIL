from collections import deque


def group(nums):
    que = deque([nums])
    used = [[[] for _ in range(1000)] for _ in range(1000)]
    used[nums[0]][nums[1]].append(nums[:])
    while que:
        x, y, z = que.popleft()
        if x == y and x == z:
            return 1

        if x != y:
            ny = y -x
            nx = x + x
            n = [nx, ny, z]
            n.sort()

            if n not in used[n[0]][n[1]]:
                used[n[0]][n[1]].append(n[:])
                que.append(n)

        if x != z:
            nz = z - x
            nx = x + x
            n = [nx, y, nz]
            n.sort()

            if n not in used[n[0]][n[1]]:
                used[n[0]][n[1]].append(n[:])
                que.append(n)
    return 0


num_list = list(map(int, input().split()))
num_list.sort()

if sum(num_list) % 3:
    print(0)
else:
    print(group(num_list[:]))
