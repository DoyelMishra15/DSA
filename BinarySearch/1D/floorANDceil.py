#floor ceil 
arr=list(map(int,input().split()))
x=int(input())
n=len(arr)
def ceil(arr,x,n):
  ans=n
  l,r=0,n-1
  while l<=r:
    mid=(l+r)//2
    if arr[mid]>=x:
      ans=mid
      r=mid-1
    else:
      l=mid+1
  return ans
def floor(arr,x,n):
  ans=-1
  l,r=0,n-1
  while l<=r:
    mid=(l+r)//2
    if arr[mid]<=x:
      ans=mid
      l=mid+1
    else:
      r=mid-1
  return ans
print(arr[floor(arr,x,n)],arr[ceil(arr,x,n)])
