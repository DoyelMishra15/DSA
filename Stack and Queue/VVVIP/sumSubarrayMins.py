class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod=10**9+7
        total = 0
        nse=[-1]*n
        s=[]
        for i in range(n-1,-1,-1):
            while s and arr[s[-1]]>=arr[i]:
                s.pop()
            if not s:
                nse[i]=n
            else:
                nse[i]=s[-1]
            s.append(i)
        s=[]
        pse=[-1]*n
        for i in range(n):
            while s and arr[s[-1]]>arr[i]:
                s.pop()
            if not s:
                pse[i]=-1
            else:
                pse[i]=s[-1]
            s.append(i)
        for i in range(n):
            lft=i-pse[i]
            right=nse[i]-i
            total=(total+((right*lft*arr[i])%mod))%mod
        return total
