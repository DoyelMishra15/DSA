def max_subarray_sum(arr):
    curr_sum = 0
    max_sum = float('-inf')

    for num in arr:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max_sum
