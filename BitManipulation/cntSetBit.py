#Count the Number of Set Bits
n=int(input())
def cnt(n):
  c=0
  while n>0:
    d=n%2
    if d==1:
      c+=1
    n=n>>1
  return c
print(cnt(n))
