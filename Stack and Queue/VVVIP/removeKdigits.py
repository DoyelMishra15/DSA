class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        s=[]
        for i in num:
            while s and i<s[-1] and k>0:
                s.pop()
                k-=1
            s.append(i)
        while k>0:
            s.pop()
            k-=1
        res=''.join(s)
        res=res.lstrip('0')
        if not res:
            return "0"
        return res
