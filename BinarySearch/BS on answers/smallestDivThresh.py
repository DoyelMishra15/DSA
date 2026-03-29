#Find the Smallest Divisor Given a Threshold

def can(arr,mid,k,n):
  s=0
  for i in arr:
    if i%mid!=0:
      s+=(i//mid)+1 
    else:
      s+=(i//mid)
  return s
  
def see(arr,k,n):
  ans=-1
  l,r=min(arr),max(arr)
  while l<=r:
    mid=(l+r)//2
    if can(arr,mid,k,n)<=k:
      ans=mid
      r=mid-1
    else:
      l=mid+1
  return ans
arr=list(map(int,input().split()))
k=int(input())
print(see(arr,k,len(arr)))
