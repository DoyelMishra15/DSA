n=int(input())
res=''
while n>0:
  d=n%2
  res=str(d)+res
  n//=2
print(res)
