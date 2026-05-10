class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans=0
        maxlen=1
        d={}
        i=0
        for j in range(len(s)):
            while s[j] in d:
                if d[s[i]]-1==0:
                    del d[s[i]]
                else:
                    d[s[i]]-=1
                i+=1
            d[s[j]]=1
            maxlen=max(maxlen,j-i+1)
        return maxlen
