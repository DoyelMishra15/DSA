def check(arr,mid,k,n):
  cnt=1 
  last=arr[0]
  for i in range(1,n):
    if arr[i]-last>=mid:
      cnt+=1 
      last=arr[i]
  return cnt>=k
  
n,k=map(int,input().split())
arr=list(map(int,input().split(',')))
arr.sort()
l,r=0,arr[-1]-arr[0]
ans=-1
while l<=r:
  mid=(l+r)//2
  if check(arr,mid,k,n):
    ans=mid
    l=mid+1 
  else:
    r=mid-1
print(ans)
