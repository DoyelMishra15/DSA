def checkSubsequence(arr, index, current_sum, k):

    if index == len(arr):
        return current_sum == k

    if checkSubsequence(arr, index + 1, current_sum + arr[index], k):
        return True

    if checkSubsequence(arr, index + 1, current_sum, k):
        return True

    return False


arr = [1, 2, 1]
k = 2

print(checkSubsequence(arr, 0, 0, k))
