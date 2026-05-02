def single_number(arr):
    xor = 0
    for num in arr:
        xor ^= num
    return xor
