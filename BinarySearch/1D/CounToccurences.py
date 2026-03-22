#Count Occurrences in Sorted Array
arr=list(map(int,input().split()))
x=int(input())
n=len(arr)
ans=n
l,r=0,n-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]>=x:
        ans=mid
        r=mid-1
    else:
        l=mid+1
ans1=n
l,r=0,n-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]>x:
        ans1=mid
        r=mid-1
    else:
        l=mid+1
if ans == n or arr[ans] != x:
    print(0)
else:
  print(ans1 - ans)
