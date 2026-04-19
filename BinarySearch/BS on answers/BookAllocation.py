def check(arr, mid, k, n):
    cnt = 1
    pages = 0

    for i in range(n):
        if pages + arr[i] <= mid:
            pages += arr[i]
        else:
            cnt += 1
            pages = arr[i]

    return cnt <= k


n, k = map(int, input().split())
arr = list(map(int, input().split(',')))

if k > n:
    print(-1)
else:
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
