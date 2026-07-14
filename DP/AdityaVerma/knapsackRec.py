wt=[1,3,4,5]
val=[1,4,5,7]
w=7
n=len(wt)
ans=-2**31
def rec(i,wt,val,curr,v):
    global ans
    if curr > w:
        return
    if i>=n:
        ans=max(ans,v)
        return
    rec(i+1,wt,val,curr+wt[i],v+val[i])
    rec(i+1,wt,val,curr,v)
if n==0 or w==0:
    print(0)
else:
    rec(0,wt,val,0,0)
    print(ans)
