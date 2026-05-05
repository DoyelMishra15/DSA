arr=[102,4,100,1,101,3,2,1,1]
mlen=1 
arr=sorted(set(arr))
print(arr)
curr=1
for i in range(len(arr)-1):
  if arr[i]+1==arr[i+1]:
    curr+=1 
  else:
    mlen=max(curr,mlen)
    curr=1
mlen=max(curr,mlen)
print(mlen)
