import sys
input = sys.stdin.readline

for tc in range(int(input())):
    N, M = map(int, input().split())
    books = [1] * (N + 1)
    hopes = []

    for i in range(M):
        a, b = map(int, input().split())
        hopes.append((a, b))

    # 끝 번호를 기준으로 희망 번호 정렬
    hopes.sort(key=lambda x: x[1])

    ans = 0
    for a, b in hopes:
        # 희망 번호 중 가장 앞에 있는 남은 책 순서로 제공
        for n in range(a, b + 1):
            # 책이 존재하면 제공 후 품절 처리
            # 품절인 경우 스킵
            if books[n]:
                books[n] = 0
                ans += 1
                break

    print(ans)
