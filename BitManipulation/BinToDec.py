n=int(input())
n=str(n)
x=0
res=0
for i in n[::-1]:
  res=res+(int(i)*(2**x))
  x+=1
print(res)
