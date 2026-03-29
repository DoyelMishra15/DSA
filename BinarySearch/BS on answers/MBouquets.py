#Minimum days to make M bouquets

def can(arr,mid,n,m,k):
  cnt=0
  boq=0
  for i in range(n):
    if arr[i]<=mid:
      cnt+=1 
    else:
      boq+=cnt//k
      cnt=0
  boq+=cnt//k
  return boq>=m

def see(arr,m,k):
  n=len(arr)
  if m*k>n:
    return -1
  else:
    ans=-1
    l,r=min(arr),max(arr)
    while l<=r:
      mid=(l+r)//2
      if can(arr,mid,n,m,k):
        ans=mid
        r=mid-1
      else:
        l=mid+1 
    return ans
arr=list(map(int,input().split()))
m,k=map(int,input().split())
print(see(arr,m,k))
