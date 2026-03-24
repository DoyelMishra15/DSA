#nth root

n=int(input())
m=int(input())
l,r=1,m
while l<=r:
  mid=(l+r)//2
  ans = 1
  for _ in range(n):
    ans *= mid
    if ans > m:
      break
  if ans==m:
    print(mid)
    break
  if ans<m:
    l=mid+1 
  else:
    r=mid-1
else:
  print(-1)
