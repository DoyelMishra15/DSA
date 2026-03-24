#Finding Sqrt of a number using Binary Search

n=int(input())
l,r=0,n 
while l<=r:
  mid=(l+r)//2 
  if mid*mid==n:
    print(mid) 
    break
  if mid*mid<n:
    l=mid+1 
  else:
    r=mid-1
