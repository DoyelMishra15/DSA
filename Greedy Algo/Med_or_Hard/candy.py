#bruteforce

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        left=[0]*n
        left[0]=1
        las=1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                las+=1
                left[i]=las
            elif ratings[i]<=ratings[i-1]:
                las=1
                left[i]=las
        right=[0]*n
        right[-1]=1
        las=1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                las+=1
                right[i]=las
            elif ratings[i]<=ratings[i+1]:
                las=1
                right[i]=las
        tot=0
        for i in range(n):
            tot = tot+max(left[i],right[i])
        return tot



#optimal

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        peak=down=0
        i=1
        sum0=1
        while i<n:
            if ratings[i]==ratings[i-1]:
                sum0+=1
                i+=1
                continue
            peak=1
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                sum0+=peak
                i+=1
            down=1
            while i<n and ratings[i]<ratings[i-1]:
                sum0+=down
                down+=1
                i+=1
            if down>peak:
                sum0+=(down-peak)
        return sum0
