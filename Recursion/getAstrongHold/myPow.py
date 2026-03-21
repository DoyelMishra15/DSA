class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n= -n
        ans=1
        t=x
        while n>0:
            if n&1==1:
                ans=ans*t
            t=t*t
            n=n>>1
        return ans
        
