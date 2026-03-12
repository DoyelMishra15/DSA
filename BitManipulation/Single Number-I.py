#Find the number that appears once, and the other numbers twice
nums=list(map(int,input().split())
ans=0
for i in nums:
  ans=ans^i
return ans
