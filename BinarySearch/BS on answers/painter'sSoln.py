def check(arr, mid, k, n):
    cnt = 1
    total = 0

    for i in range(n):
        if total + arr[i] <= mid:
            total += arr[i]
        else:
            cnt += 1
            total = arr[i]

    return cnt <= k


n, k = map(int, input().split())
arr = list(map(int, input().split(',')))

l, r = max(arr), sum(arr)
ans = -1

while l <= r:
    mid = (l + r) // 2

    if check(arr, mid, k, n):
        ans = mid
        r = mid - 1  
    else:
        l = mid + 1

print(ans)
