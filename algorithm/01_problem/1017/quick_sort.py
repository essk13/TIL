def partition(min_, max_):
    p = arr[min_]
    mi, ma = min_, max_
    while mi <= ma:
        while mi <= ma and p >= arr[mi]:
            mi += 1
        while mi <= ma and p <= arr[ma]:
            ma -= 1
        if mi < ma:
            arr[mi], arr[ma] = arr[ma], arr[mi]
    arr[min_], arr[ma] = arr[ma], arr[min_]
    return ma


def quick_sort(min_, max_):
    if min_ >= max_: return
    p = partition(min_, max_)
    quick_sort(min_, p-1)
    quick_sort(p+1, max_)


arr = list(map(int, input().split()))
N = len(arr)
quick_sort(0, N-1)
print(*arr)
