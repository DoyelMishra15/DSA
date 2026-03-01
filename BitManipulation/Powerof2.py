#Check if a Number is Power of 2 or Not
n=int(input())
def pow(n):
  return (n&(n-1)==0)
print(pow(n))
