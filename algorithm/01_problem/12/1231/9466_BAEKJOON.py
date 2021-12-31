import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


def check(now):
    global ans
    # 현재 학생 확인완료 처리
    checked[now] = 1
    # 현재 학생 등록
    ck.append(now)
    # 현재 학생이 지목한 학생 확인
    target = students[now]

    # 지목한 학생의 확인완료 여부 판단
    if checked[target]:
        # 지목한 학생의 등록 여부 판단
        if target in ck:
            # 등록된 경우 지목된 학생이 첫번째여야 함으로 해당 학생부터 뒤까지 팀 결성
            # 팀 미결성 인원에서 결성 인원 수 제거
            ans -= len(ck[ck.index(target):])
        return

    check(target)


for tc in range(int(input())):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    checked = [0] * (n + 1)
    ans = n
    for st in range(1, n + 1):
        if not checked[st]:
            # 이미 확인한 학생은 재확인 X
            ck = []
            check(st)

    print(ans)
