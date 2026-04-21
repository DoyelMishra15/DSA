class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        c=sorted(d,key= lambda x : d[x],reverse=True)
        ans=""
        for i in c:
            ans+= i*d[i]
        return ans
