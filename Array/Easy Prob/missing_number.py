def missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)
