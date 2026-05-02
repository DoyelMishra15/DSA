def left_rotate_k(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]
