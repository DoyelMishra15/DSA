def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num != first and num > second:
            second = num
    return second if second != float('-inf') else -1
