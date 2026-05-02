def max_consecutive_ones(arr):
    count = maxi = 0
    for num in arr:
        if num == 1:
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
    return maxi
