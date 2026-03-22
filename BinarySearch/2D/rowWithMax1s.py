#Find the row with maximum number of 1's
arr=[]

# n=int(input())
# for _ in range(n):
#   arr.append(list(map(int,input().split())))

//brute force

# idx=-1
# max1=0
# for i in range(n):
#   cnt=0
#   for j in range(n):
#     if arr[i][j]==1:
#       cnt+=1 
#   if cnt>max1:
#     max1=cnt
#     idx=i
# print(idx)


#optimized

#Find the row with maximum number of 1's
arr=[]
n=int(input())

for _ in range(n):
  arr.append(list(map(int,input().split())))

idx=-1
max1=0

for i in range(n):
  ans=len(arr[0])
  l,r=0,len(arr[0])-1
  
  while l<=r:
    mid=(l+r)//2
    if arr[i][mid]==1:
      ans=mid
      r=mid-1 
    else:
      l=mid+1
  
  if max1<len(arr[0])-ans:
    max1=len(arr[0])-ans
    idx=i

print(idx)
