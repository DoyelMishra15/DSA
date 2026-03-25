#Search Element in a Rotated Sorted Array with duplicates

arr=list(map(int,input().split()))
x=int(input())

def ans(arr,x):
  l,r=0,len(arr)-1
  while l<=r:
    mid=(l+r)//2
    if arr[mid]==x:
      return mid
    if arr[l]==arr[mid]==arr[r]:
      l+=1 
      r-=1 
    elif arr[l]<=arr[mid]:
      if arr[l] <= x < arr[mid]:
        r =mid-1
      else:
        l=mid+1
    else:
      if arr[mid] < x <= arr[r]:
        r =mid-1
      else:
        l=mid+1
  else:
    return -1
    
print(ans(arr,x))
