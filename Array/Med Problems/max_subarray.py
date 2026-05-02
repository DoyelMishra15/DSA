def max_subarray(arr):
    curr_sum = 0
    max_sum = float('-inf')
    start = end = s = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = s
            end = i

        if curr_sum < 0:
            curr_sum = 0
            s = i + 1

    return arr[start:end+1]
