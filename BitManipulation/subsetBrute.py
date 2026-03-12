#78. Subsets

l=list(map(int,input().split()))
n=len(l)
subsets=1<<n
ans=[]

#print(n)

for i in range(0,subsets):
  temp=[]
  for j in range(n):
    if i&(1<<j):
      temp.append(l[j])
  ans.append(temp)
print(*ans)
