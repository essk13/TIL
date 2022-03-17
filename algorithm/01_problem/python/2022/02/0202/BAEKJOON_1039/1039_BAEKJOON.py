from collections import deque


def change():
    res = -1
    # n번 움직인 상태에서 해당 숫자가 나온 적인 있는지 확인을 위한 배열
    used = [[] for _ in range(K + 1)]
    que = deque([[N[:] , 0]])
    while que:
        n, cnt = que.popleft()
        if cnt == K:
            res = max(res, int(''.join(n)))
            continue

        for i in range(len(N)):
            for j in range(i+1, len(N)):
                # 첫째 자리가 0으로 시작 불가
                if i == 0 and n[j] == '0': continue
                new = n[:]
                new[i], new[j] = new[j], new[i]
                # 해당 숫자가 해당 횟수에 존재하지 않으면 수행
                if new not in used[cnt+1]:
                    que.append([new, cnt + 1])
                    used[cnt+1].append(new)
    return res


N, K = map(int, input().split())
N = list(str(N))

print(change())
