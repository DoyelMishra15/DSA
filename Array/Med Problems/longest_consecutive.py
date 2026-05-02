def longest_consecutive(arr):
    s = set(arr)
    longest = 0

    for num in s:
        if num - 1 not in s: 
            curr = num
            count = 1

            while curr + 1 in s:
                curr += 1
                count += 1

            longest = max(longest, count)

    return longest
