# find the peak element

arr = list(map(int, input().split(',')))
n = len(arr)
def ans(arr, n):
    l = 0
    r = n - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > arr[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l
print(ans(arr, n))
