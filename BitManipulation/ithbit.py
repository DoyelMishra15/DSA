#Check if the i-th bit is set or not
n=int(input())
i=int(input())
def ithbit(n,i):
  return ((n>>i)&1==1)
print(ithbit(n,i))
