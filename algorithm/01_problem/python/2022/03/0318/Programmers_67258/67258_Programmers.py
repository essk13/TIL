import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    gems = list(input().split())
    list_g = list(set(gems))
    stn = len(list_g)
    edn = len(gems)
