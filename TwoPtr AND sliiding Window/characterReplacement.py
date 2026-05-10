class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            has=[0]*26
            maxf=0
            for j in range(i,n):
                has[ord(s[j])-65]+=1
                maxf=max(maxf,has[ord(s[j])-65])
                changes=j-i+1-maxf
                if changes<=k:
                    ans=max(ans,j-i+1)
                else:
                    break
        return ans

  class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        maxlen=maxf=0
        d = {}
        l=r=0
        while l<n and r<n:
            d[s[r]]=d.get(s[r],0)+1
            maxf=max(d.values())
            if r-l+1-maxf<=k:
                maxlen=max(maxlen,r-l+1)
            else:
                while r-l+1-maxf>k:
                    d[s[l]]-=1
                    if d[s[l]]==0:
                        del d[s[l]]
                    l+=1
            r+=1
        return maxlen

    class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        maxlen=maxf=0
        d = {}
        l=r=0
        while l<n and r<n:
            d[s[r]]=d.get(s[r],0)+1
            maxf=max(d.values())
            if r-l+1-maxf<=k:
                maxlen=max(maxlen,r-l+1)
            else:
                while r-l+1-maxf>k:
                    d[s[l]]-=1
                    if d[s[l]]==0:
                        del d[s[l]]
                    l+=1
                maxf=max(d.values())
            r+=1
        return maxlen
