#Minimise Maximum Distance between Gas Stations

def check(arr, mid, k, n):
    cnt = 0

    for i in range(1, n):
        gap = arr[i] - arr[i-1]
        cnt += int(gap // mid)

    return cnt <= k


n, k = map(int, input().split())
arr = list(map(int, input().split(',')))

l, r = 0, arr[-1] - arr[0]

for _ in range(100):
    mid = (l + r) / 2

    if check(arr, mid, k, n):
        r = mid
    else:
        l = mid

print(r)
