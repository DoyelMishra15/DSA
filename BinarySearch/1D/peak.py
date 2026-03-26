#find the peak element

arr=list(map(int,input().split(',')))
n=len(arr)
def ans(arr,n):
  if sorted(arr)==arr:
    return 0
  if sorted(arr,reverse=True)==arr:
    return n-1
  l=1
  r=n-2
  while l<=r:
    mid=(l+r)//2 
    if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
      return mid
    elif arr[mid]<arr[mid+1]:
      l=mid+1 
    else:
      r=mid-1
  else:
    return -1
print(ans(arr,n))
