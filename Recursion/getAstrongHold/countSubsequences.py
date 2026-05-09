def countSubsequences(arr, index, current_sum, k):
    
    if index == len(arr):
        if current_sum == k:
            return 1
        return 0

    left = countSubsequences(arr, index + 1, current_sum + arr[index], k)
    right = countSubsequences(arr, index + 1, current_sum, k)

    return left + right


arr = [1, 2, 1]
k = 2

print(countSubsequences(arr, 0, 0, k))
