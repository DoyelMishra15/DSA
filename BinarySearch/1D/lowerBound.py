#lower bound, also ceil
arr=list(map(int,input().split()))
x=int(input())
n=len(arr)
l,r=0,n-1
ans=0
while l<=r:
  mid=(l+r)//2
  if arr[mid]>=x:
    ans=mid
    r=mid-1
  else:
    l=mid+1
print(ans)
