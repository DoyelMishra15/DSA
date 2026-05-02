def leaders(arr):
    n = len(arr)
    max_right = arr[-1]
    result = [max_right]

    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            result.append(arr[i])
            max_right = arr[i]

    return result[::-1]
