class Solution:
    def subArrayRanges(self, arr: List[int]) -> int:
        n=len(arr)
        small = 0
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
            small += right*lft*arr[i]
        nge=[-1]*n
        s=[]
        for i in range(n-1,-1,-1):
            while s and arr[s[-1]]<=arr[i]:
                s.pop()
            if not s:
                nge[i]=n
            else:
                nge[i]=s[-1]
            s.append(i)
        s=[]
        pge=[-1]*n
        for i in range(n):
            while s and arr[s[-1]]<arr[i]:
                s.pop()
            if not s:
                pge[i]=-1
            else:
                pge[i]=s[-1]
            s.append(i)
        r=0
        for i in range(n):
            lft=i-pge[i]
            right=nge[i]-i
            r += right*lft*arr[i]
        return r-small
