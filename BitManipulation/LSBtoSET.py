#Set the rightmost bit
#Set the rightmost bit
n = int(input())
def setRightmostZero(n):
  if (n & (n + 1)) == 0:
    return n
  return n | (n + 1)
print(setRightmostZero(n))
