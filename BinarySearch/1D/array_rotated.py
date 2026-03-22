#How many times Array is rotated
arr=list(map(int,input().split()))
n=len(arr)
l,r=0,n-1
while l<r:
    mid=(l+r)//2
    if arr[mid]>arr[r]:
        l=mid+1
    else:
        r=mid
print(l)
