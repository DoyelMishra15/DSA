class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            cnt=0
            d={}
            for j in range(i,len(s)):
                d[s[j]]=d.get(s[j],0)+1
                cnt=max(d.values())-min(d.values())
                ans+=cnt
        return ans
        
