#Find XOR of numbers from L to R

l, r = map(int,input().split())
ans=l
for i in range(l+1,r+1):
  ans= ans^i
print(ans)


#Find XOR of numbers from L to R

l, r = map(int,input().split())
n=r-l+1
ans=0
def xor(n):
  if n%4==1:
    ans=1 
  elif n%4==2:
    ans=n+1
  elif n%2==3:
    ans = 0
  else:
    ans = n
  return ans
print(xor(l-1)^xor(r))
