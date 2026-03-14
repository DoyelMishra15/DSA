#Print all Divisors of a given Number

n=int(input())
res=[]
for i in range(1,int(n**0.5)+1):
  if n%i==0:
    res.append(i)
  if i*i!=n:
    res.append(n//i)
print(res)
