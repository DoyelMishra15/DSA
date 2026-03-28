#Koko Eating Bananas

arr=list(map(int,input().split(',')))
h=int(input())
l,r=1,max(arr)
ans=0
def can(arr,mid):
  cnt=0
  for i in range(len(arr)):
    if arr[i]%mid!=0:
      cnt+=(arr[i]//mid)+1
    else:
      cnt+= arr[i]//mid
  if cnt<=h:
    return True
  return False
while l<=r:
  mid=(l+r)//2
  if can(arr,mid):
    ans=mid
    r=mid-1
  else:
    l=mid+1
print(ans)
