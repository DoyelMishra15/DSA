wt=[1,3,4,5]
val=[1,4,5,7]
w=7
ans=-2**31
def rec(i,wt,val,curr,v):
    global ans
    if curr > w:
        return
    if i>=len(wt):
        ans=max(ans,v)
        return
    p=rec(i+1,wt,val,curr+wt[i],v+val[i])
    np=rec(i+1,wt,val,curr,v)
rec(0,wt,val,0,0)
print(ans)
