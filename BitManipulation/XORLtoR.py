#Find XOR of numbers from L to R

l, r = map(int,input().split())
ans=l
for i in range(l+1,r+1):
  ans= ans^i
print(ans)
