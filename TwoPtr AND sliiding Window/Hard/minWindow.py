#bruteforce
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlen=10**9
        sindex=-1
        n=len(s)
        m=len(t)
        for i in range(n):
            has=[0]*256
            cnt=0
            for j in range(m):
                has[ord(t[j])]+=1
            for j in range(i,n):
                if has[ord(s[j])]>0:
                    cnt+=1
                has[ord(s[j])]-=1
                if cnt==m:
                    if j-i+1<minlen:
                        minlen=j-i+1
                        sindex=i
                    break
            if sindex==-1:
                return ""
        return s[sindex:sindex+minlen]
      
  
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        d1 = {}
        for ch in t:
            d1[ch] = d1.get(ch, 0) + 1
        i = 0
        cnt = 0
        minlen = float('inf')
        start = 0
        for j in range(len(s)):
            if s[j] in d1:
                if d1[s[j]] > 0:
                    cnt += 1
                d1[s[j]] -= 1
            while cnt == len(t):
                if j - i + 1 < minlen:
                    minlen = j - i + 1
                    start = i
                if s[i] in d1:
                    d1[s[i]] += 1
                    if d1[s[i]] > 0:
                        cnt -= 1
                i += 1
        if minlen == float('inf'):
            return ""
        return s[start:start + minlen]



