arr=[102,4,100,1,101,3,2,1,1]
def lcs(arr):
  n=len(arr)
  if n==0:
    return 0
  mlen=1 
  swt=set(arr)
  for i in swt:
    if i-1 not in swt:
      cnt=1 
      x=i 
      while x+1 in swt:
        cnt+=1 
        x+=1
      mlen=max(cnt,mlen)
  return mlen
print(lcs(arr))
